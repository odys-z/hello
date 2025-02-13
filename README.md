
[![Ukraine](https://cdn3.emoji.gg/emojis/6101-ukraine.gif)](https://emoji.gg/emoji/6101-ukraine)

## About Hello

The Helloworld projects for tests.

### Troubleshootings

How to deal with unstable github connection when cloning a repository.

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