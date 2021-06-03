# Quick Start

pip install -U sphinx

- run powershell as administrator

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

choco install make
```

- make _build/html/index.html

```
make html
```

- install sphinx rtd theme

```
install sphinx rtd theme
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

- Get start

Add a title, sub-title, doc tree, link, code-block and image.
