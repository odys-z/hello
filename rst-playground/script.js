// Live rST playground, Sphinx edition: <base> + blob.
//
//   Start-up -> every file in sphinx/manifest.json copied from sphinx/source/ into Pyodide
//   Run -> textarea saved as index.rst -> sphinx-build in Pyodide -> build/html/index.html
//       -> <base href="ASSETS_BASE"> added -> page put in a Blob -> iframe shows the blob.
//
// The built page refers to its resources by relative paths (_static/css/theme.css,
// _images/x.png, ...). A blob page has no address of its own to resolve them against, so
// <base> points them at a folder that already holds the same files: what `make ghpage` deployed.
//
// Layout (hello/ and odys-z.github.io/ side by side; the three sphinx/ entries are symlinks):
//   hello/rst-playground/
//     index.xhtml, script.js, style.css, start_with_manifest.py
//     sphinx/manifest.json   written by start_with_manifest.py
//     sphinx/source  -> ../../../odys-z.github.io/sphinx/products/portfolio/source
//     sphinx/_static -> ../../../odys-z.github.io/products/portfolio/_static
//     sphinx/_images -> ../../../odys-z.github.io/products/portfolio/_images

const inputTextarea = document.getElementById("rst-input");
const outputFrame = document.getElementById("html-output");
const runButton = document.getElementById("run");
const statusText = document.getElementById("status");

// Folder holding the deployed _static/ and _images/, ending with "/". Either the symlinked
// copies in sphinx/ (same origin: always works), or the live site,
// "https://odys-z.github.io/products/portfolio/". Fonts from another origin load only if it
// sends "Access-Control-Allow-Origin: *"; check once in DevTools.
const ASSETS_BASE = new URL("sphinx/", location.href).href;

// List of source files to load, written by start_with_manifest.py.
const MANIFEST_URL = new URL("sphinx/manifest.json", location.href).href;

// Folders in Pyodide's in-memory filesystem, as in the Makefile's English build:
//   sphinx-build -b html -d build/doctrees source build/html
const SRC = "/sphinx/source";
const OUT = "/sphinx/build/html";
const DOCTREES = "/sphinx/build/doctrees";

const PACKAGES = ["sphinx", "sphinx_rtd_theme", "sphinxcontrib-video"];

const setStatus = (text) => (statusText.textContent = text);
const seconds = (since) => ((performance.now() - since) / 1000).toFixed(1) + " s";

// ---------------------------------------------------------------- start-up

async function main() {
  const start = performance.now();

  setStatus("Loading Pyodide…");
  const pyodide = await loadPyodide();

  setStatus("Installing Sphinx and the theme…");
  await pyodide.loadPackage("micropip");
  const micropip = pyodide.pyimport("micropip");
  await micropip.install(PACKAGES);
  micropip.destroy();
  // A package that fails to download is only logged by Pyodide, not thrown:
  // import everything now, so a broken install fails here instead of at the first Run.
  pyodide.runPython("import sphinx, sphinx_rtd_theme, sphinxcontrib.video, docutils, jinja2, pygments");

  setStatus("Loading the Sphinx source…");
  const count = await loadSource(pyodide);

  // Start from the current index.rst on disk. Always overwrite: on reload the browser may
  // restore the textarea's old text, which would hide changes made to the file.
  inputTextarea.value = pyodide.FS.readFile(`${SRC}/index.rst`, { encoding: "utf8" });

  setStatus(`Ready in ${seconds(start)}, ${count} source files loaded. Edit index.rst and press Run.`);
  runButton.disabled = false;
  return pyodide;
}

// Copies every file listed in the manifest into Pyodide, keeping the folder layout:
// sphinx/source/android/index.rst -> /sphinx/source/android/index.rst.
// conf.py is your real one; its exclude_patterns skip the language folders, which the
// manifest leaves out anyway. Sphinx still copies static/custom.css into its own
// build/html/_static/, unused by the preview; add_css_file() in conf.py puts its <link> in the page.
async function loadSource(pyodide) {
  const manifestResponse = await fetch(MANIFEST_URL, { cache: "no-cache" });
  if (!manifestResponse.ok) {
    throw new Error(`Cannot load ${MANIFEST_URL}: ${manifestResponse.status}. Run start_with_manifest.py first.`);
  }
  const manifest = await manifestResponse.json();
  const sourceUrl = new URL(manifest.source, location.href); // "sphinx/source/", relative to this page

  await Promise.all(manifest.files.map(async (file) => {
    const url = new URL(file, sourceUrl);
    const response = await fetch(url, { cache: "no-cache" }); // always check for a newer copy
    if (!response.ok) throw new Error(`Cannot load ${url}: ${response.status}`);
    const path = `${SRC}/${file}`;
    pyodide.FS.mkdirTree(path.slice(0, path.lastIndexOf("/")));
    pyodide.FS.writeFile(path, new Uint8Array(await response.arrayBuffer()));
  }));
  return manifest.files.length;
}

const pyodideReadyPromise = main();
pyodideReadyPromise.catch((err) => setStatus(`Start-up failed: ${err.message ?? err}`));


// ---------------------------------------------------------------- Run

runButton.addEventListener("click", rstToHtml);

async function rstToHtml() {
  runButton.disabled = true;
  try {
    const pyodide = await pyodideReadyPromise;

    const start = performance.now();
    setStatus("Building…");
    pyodide.FS.writeFile(`${SRC}/index.rst`, inputTextarea.value);
    const log = build(pyodide);

    showBuiltPage(pyodide, "index.html");

    const warnings = log.trim() ? log.trim().split("\n").length : 0;
    setStatus(`Built in ${seconds(start)}, ${warnings} warning line(s).`);
    if (warnings) console.warn(log);
  } catch (err) {
    setStatus("Failed, see the preview.");
    const pre = document.createElement("pre");
    pre.textContent = err.message ?? String(err);
    showPage("<!DOCTYPE html>\n" + pre.outerHTML);
  } finally {
    runButton.disabled = false;
  }
}

// Same arguments as the Makefile; -q leaves only warnings and errors, captured for the status line.
function build(pyodide) {
  const result = pyodide.runPython(`
import io, contextlib
from sphinx.cmd.build import build_main

_log = io.StringIO()
with contextlib.redirect_stdout(_log), contextlib.redirect_stderr(_log):
    _rc = build_main(["-b", "html", "-q", "-d", "${DOCTREES}", "${SRC}", "${OUT}"])
(_rc, _log.getvalue())
`);
  const [exitCode, log] = result.toJs();
  result.destroy();
  if (exitCode !== 0) throw new Error(`sphinx-build failed (exit code ${exitCode})\n\n${log}`);
  return log;
}

// ---------------------------------------------------------------- iframe

// The built pages live in Pyodide (build/html/), not on the server. Each one is shown as a
// blob, with <base> set to the matching folder under ASSETS_BASE, so that "../_static/..."
// in android/index.html still finds sphinx/_static/.
let currentPage = "index.html"; // path inside build/html/ of the page on show
let pendingHash = "";           // #fragment to scroll to once that page has loaded

function showBuiltPage(pyodide, page, hash = "") {
  const html = pyodide.FS.readFile(`${OUT}/${page}`, { encoding: "utf8" });
  const base = new URL(page.replace(/[^/]*$/, ""), ASSETS_BASE).href; // "android/index.html" -> .../sphinx/android/
  currentPage = page;
  pendingHash = hash;
  showPage(html.replace("<head>", `<head>\n<base href="${base}">`));
}

let pageUrl = null; // blob URL of the page on show

function showPage(html) {
  const previous = pageUrl;
  pageUrl = URL.createObjectURL(new Blob([html], { type: "text/html" }));
  outputFrame.src = pageUrl;
  // Free the previous page once the new one has replaced it.
  if (previous) outputFrame.addEventListener("load", () => URL.revokeObjectURL(previous), { once: true });
}

// The blob page has this page's origin, so its clicks can be handled here. Without this,
// a link such as "about.html" resolves against <base> and asks the server for
// sphinx/about.html, which only exists in Pyodide.
outputFrame.addEventListener("load", () => {
  const doc = outputFrame.contentDocument;
  if (!doc) return;
  doc.addEventListener("click", onPreviewClick);
  doc.addEventListener("submit", onPreviewSubmit);
  scrollToHash(doc, pendingHash);
  pendingHash = "";
});

async function onPreviewClick(event) {
  const link = event.target.closest?.("a[href]");
  if (!link || event.defaultPrevented) return;
  const href = link.getAttribute("href");
  event.preventDefault();

  // Other sites (Sphinx, Read the Docs, the Play Store badge link...): open in a new tab.
  if (/^[a-z][a-z0-9+.-]*:/i.test(href) || href.startsWith("//")) {
    window.open(link.href, "_blank", "noopener");
    return;
  }

  const [pathPart, hash = ""] = href.split("#");
  let target = currentPage;
  if (pathPart) {
    target = new URL(pathPart, "file:///" + currentPage).pathname.slice(1); // resolve "../about.html"
    if (target.endsWith("/") || target === "") target += "index.html";
  }

  if (target === currentPage) {
    scrollToHash(outputFrame.contentDocument, hash); // "#section" on the same page
    return;
  }
  const pyodide = await pyodideReadyPromise;
  if (!pyodide.FS.analyzePath(`${OUT}/${target}`).exists) {
    setStatus(`Not in the preview build: ${target}`);
    return;
  }
  showBuiltPage(pyodide, target, hash);
}

// The sidebar's search box submits to search.html, which needs searchindex.js from the build.
function onPreviewSubmit(event) {
  event.preventDefault();
  setStatus("Search isn't available in the preview.");
}

function scrollToHash(doc, hash) {
  if (!doc) return;
  const target = hash && doc.getElementById(decodeURIComponent(hash));
  if (target) target.scrollIntoView();
  else doc.defaultView?.scrollTo(0, 0);
}
