
[![Ukraine](https://cdn3.emoji.gg/emojis/6101-ukraine.gif)](https://emoji.gg/emoji/6101-ukraine)

## About Hello

The Helloworld projects for tests.

### Troubleshootings

- How to deal with unstable github connection when cloning a repository.

```
    unzip <repo>.zip
    cd <repo>
    git init
    git add .
    git remote add origin https://github.com/<user>/<repo>.git
    git remote update
    git checkout master
```

See [arctelix' answer](https://stackoverflow.com/questions/15681643/how-to-clone-git-repository-from-its-zip)

- Tocken verification

```
    curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/repos/odys-z/hello
```

- Fix git's HTTP transport

The disconnects usually come from git's default HTTP buffer being too small for a big pack, or an unstable connection dropping HTTP/2 streams. Run these once, globally:

bash
``` git config --global http.postBuffer 1048576000
    git config --global http.lowSpeedLimit 0
    git config --global http.lowSpeedTime 999999
    git config --global http.version HTTP/1.1
```

  - http.postBuffer — raises the buffer git uses for large transfers (fixes "unexpected disconnect while reading sideband packet" specifically)

  - http.lowSpeedLimit/http.lowSpeedTime — stops git from aborting a slow-but-alive transfer

  - http.version HTTP/1.1 — HTTP/2 multiplexing sometimes chokes on corporate proxies/VPNs/flaky Wi-Fi; forcing 1.1 is a common fix for exactly this GitHub clone symptom
