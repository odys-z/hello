# Cat Coding — A Webview API Sample

Demonstrates VS Code's [webview API](https://code.visualstudio.com/api/extension-guides/webview). This includes:

- Load webpack watched results.
- The local http server can be started using teminal (see teminal-sample).
- Terminate python http server way 1, [kill process](https://stackoverflow.com/a/37214138/7362888):

```
    kill `ps -ef |grep http.server |grep python |awk '{print $2}'`
```

- Terminate python http server way 2, [hack the source](../../../acsl-pydev/hacking/anserv.py).

Why?

The vs code terminal extension can't receive CLI results.

Reference

- [Terminal: add a way of getting the exit code #62103](https://github.com/microsoft/vscode/issues/91016)

- [TerminalOptions.waitOnExit API #70444](https://github.com/microsoft/vscode/issues/70444)

- [Terminal API](https://code.visualstudio.com/api/references/vscode-api#Terminal)

- [How to run a system command](https://stackoverflow.com/a/64598488/7362888)

## Quick Start

- Open this example in VS Code 1.47+
- `npm install`
- `npm run watch` or `npm run compile`
- `F5` to start debugging

## Packing

```
    vsce package
```
