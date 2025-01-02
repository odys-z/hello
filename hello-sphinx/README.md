# About

*Hello-sphinx* is a [sphinx doc tool](https://www.sphinx-doc.org/en/master/) project's
setting template, optionally with [RTD theme](https://readthedocs.org/).

# Quick Start

- install sphinx

```
pip install -U sphinx
```

- run powershell as administrator

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

Or using Chocolatey on Windows (install Chocolatey first),

```
choco install make
```

Usually linux system has *make* installed natively.

- make _build/html/index.html

```
make html
```

- install sphinx rtd theme

```
pip install sphinx_rtd_theme
```

- optional: conf.py

```
BUILDDIR      = ../docs

extensions = [
    'sphinx.ext.mathjax',
    'sphinx_rtd_theme',
]
html_theme = 'sphinx_rtd_theme'
```

- getting start

Try to add a title, sub-title, doc tree, link, code-block and image.
