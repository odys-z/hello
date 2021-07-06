# Set up Prosody:

Doc: [Certificates](https://prosody.im/doc/certificates)

Doc: [using Let’s Encrypt with Prosody](https://prosody.im/doc/letsencrypt)

```
    [root@29 prosody]# vi prosody.cfg.lua
    [root@29 prosody]# firewall-cmd --zone=public --add-port=5222/tcp --permanent
    success
    [root@29 prosody]# firewall-cmd --zone=public --add-port=5222/udp --permanent
    success
    [root@29 prosody]# firewall-cmd --zone=public --add-port=5000/udp --permanent
    success
    [root@29 prosody]# firewall-cmd --zone=public --add-port=5000/tcp --permanent
    success
    [root@29 prosody]# firewall-cmd --zone=public --add-port=5269/tcp --permanent
    success
    [root@29 prosody]# firewall-cmd --zone=public --add-port=5269/udp --permanent
    success
    [root@29 prosody]# firewall-cmd --zone=public --add-port=5280/tcp --permanent
    success
    [root@29 prosody]# firewall-cmd --zone=public --add-port=5281/tcp --permanent
    success
    [root@29 prosody]# firewall-cmd --zone=public --add-port=5347/tcp --permanent
    success
    [root@29 prosody]# firewall-cmd --zone=public --add-port=5582/tcp --permanent
    success
    [root@29 prosody]# prosodyctl status
    Prosody is running with PID 19373
    [root@29 prosody]# firewall-cmd --reload
```

/etc/prosody/prosody.cfg.lua

```
    -- Location of directory to find certificates in (relative to main config file):
    certificates = "/etc/pki/prosody/"

    -- HTTPS currently only supports a single certificate, specify it here:
    https_certificate = "/etc/letsencrypt/live/..."
    https_key = "/etc/letsencrypt/live/..."
```

### extending vCard MUC

Prosody Doc:
[install prosody module](https://prosody.im/doc/installing_modules), the
[mod_muc_mam](https://prosody.im/doc/modules/mod_muc_mam)

Prerequisite: [intall Mecurial(hg)](https://www.mercurial-scm.org/wiki/Download)
This failed:

```
    yum install mecurial
    Loaded plugins: fastestmirror
    Loading mirror speeds from cached hostfile
     * base: mirrors.163.com
     * epel: ftp.iij.ad.jp
     * extras: mirrors.163.com
     * updates: mirrors.163.com
    No package mecurial available.
    Error: Nothing to do
```

But can be installed in a hack way - copy the source into modules folder(verified ok).

[source](https://modules.prosody.im/mod_vcard_muc.html)

Online verifier: [XMPP Compliance Tester](https://compliance.conversations.im/server/inforise.com.cn/)
