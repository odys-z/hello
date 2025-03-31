# Try Replace Make

[thanks to Grok](https://grok.com/chat/a1d95395-c2ff-400c-9f63-ffc3fd0199d8)


```
    pip install invoke

    $ ll
    total 47381
    drwxr-xr-x 1 Alice 197121        0 Mar 30 17:09 bin/
    -rw-r--r-- 1 Alice 197121 48505346 Mar 30 23:36 jserv-portfolio-0.7.1.zip
    lrwxrwxrwx 1 Alice 197121       72 Mar 30 22:23 portfolio-synode-0.7-py3-none-any.whl -> ../../../semantic-jserv/synode.py/dist/synode_py3-0.1.0-py3-none-any.whl
    -rw-r--r-- 1 Alice 197121      164 Mar 30 21:43 README.md
    -rw-r--r-- 1 Alice 197121     5202 Mar 30 23:24 tasks.py
    lrwxrwxrwx 1 Alice 197121       42 Mar 30 22:04 volume -> ../../../semantic-jserv/jserv-album/volume/
    lrwxrwxrwx 1 Alice 197121       52 Mar 30 22:01 web-dist -> ../../../anclient/examples/example.js/album/web-dist/
    lrwxrwxrwx 1 Alice 197121       65 Mar 30 22:03 web-inf -> ../../../semantic-jserv/jserv-album/src/main/webapp/WEB-INF-0.7.1/
    lrwxrwxrwx 1 Alice 197121       40 Mar 30 22:25 winsrv -> ../../../semantic-jserv/synode.py/winsrv/

    invoke make
```

Use mklink in Windows.