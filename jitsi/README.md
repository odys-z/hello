# About

A try to host a jitsi server.

# Quick Start

Reference:

    [Jitsi Documents](https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-docker)

Download the .gz file, then

```
    cd docker-jitsi-meet
	cp env.example .env
```

# troubleshootings

```
    Version in “./docker-compose.yml” is unsupported. You might be seeing this error because you're using the wrong Compose file version
```

See [here](https://stackoverflow.com/a/42157613/7362888)

```
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```
