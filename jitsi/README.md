# About


A try to host a jitsi server, failed in all three way, and only works on https://meet.jit.si/ .

# Docker Way

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

# Results

Failed - can't start a meet.

There are similar error reports.

```
    strophe.umd.js:5463 WebSocket connection to 'wss://localhost:8443/xmpp-websocket?room=abc' failed:
```
Guess: Nginx revers proxy dosn't pass wss requests to xmpp server (Prosody). But
this configuration can not been changed. See

[Config changes are not applied to Jitsi Meet on Docker](https://community.jitsi.org/t/config-changes-are-not-applied-to-jitsi-meet-on-docker/23978).

And [the manual way is not recommended](https://github.com/jitsi/eslint-config-jitsi/issues/17).
