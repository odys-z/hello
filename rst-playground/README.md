# rst-playground

Live preview of the Portfolio docs: Sphinx + sphinx_rtd_theme run **in the browser**
(Pyodide 0.29), styled by the deployed site's `_static/`.
Started from [Alessandro-Battiato/rst-playground](https://github.com/Alessandro-Battiato/rst-playground).

## Run

```bash
python3 start_with_manifest.py [--port 8997]
# Preview: http://localhost:8997/index.xhtml
```

## Layout

`hello/` and `odys-z.github.io/` must sit side by side (`~/github/`).

```
rst-playground/
  index.xhtml  script.js  style.css  start_with_manifest.py
  sphinx/manifest.json   generated
  sphinx/source  -> ../../../odys-z.github.io/sphinx/products/portfolio/source
  sphinx/_static -> ../../../odys-z.github.io/products/portfolio/_static
  sphinx/_images -> ../../../odys-z.github.io/products/portfolio/_images
```

Symlink targets are relative to `sphinx/`, hence three `../`.
Create each link once: a second `ln -s` puts a stray link *inside* the target folder.

## How it works

- Show: page read from `/sphinx/build/html/`, `<base href=".../sphinx/<page folder>/">` added,
   shown as a blob in the iframe. `<base>` makes `_static/`, `_images/` load from the symlinks.

- `loadPyodide()` returns a machine

A CPython interpreter with its own in-memory disk, driven through a few APIs:

| API | What it is | Used in script.js for |
|---|---|---|
| `pyodide.FS` | The machine's disk (`writeFile`, `readFile`, `mkdirTree`, `readdir`, `analyzePath`) | Loading source files, writing `index.rst`, reading built pages |
| `pyodide.runPython(code)` | Run Python, get the last expression back | Import check, `build_main` |
| `pyodide.loadPackage` / `pyimport("micropip")` | Install software on the machine | Installing Sphinx and the theme |
| `result.toJs()` / `.destroy()` | Python value → JS / free the proxy | The `(exit code, log)` tuple |

- Walled off from the OS, **not** from the page: `import js` reaches the DOM and `fetch`.
- In memory: everything is gone on reload (hence reinstall + refetch at start-up).
- Shares the page's thread: the UI waits during a build (bigger projects → Web Worker).

## Debug (DevTools console)

```js
const py = await pyodideReadyPromise;
py.FS.readdir('/sphinx/source')
py.FS.readFile('/sphinx/build/html/index.html', { encoding: 'utf8' })
```
Build warnings are printed with `console.warn` after each Run.
