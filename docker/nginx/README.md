# Firewall @ Centos 7

[CentOS: Firewall settings](https://www.printsupportcenter.com/hc/en-us/articles/360000689849-CentOS-Firewall-settings)

```
    firewall-cmd --zone=public --list-all
    firewall-cmd --zone=public --add-port=443/tcp --permanent
    firewall-cmd --reload
```

# Turn on SSL

[Issue certs with Let's Encrypt Certbot standalone]()

```
    ssl_certificate "/etc/letsencrypt/live/domain.com/fullchain.pem";
    ssl_certificate_key "/etc/letsencrypt/live/domain.com/privkey.pem";
    ssl_protocols TLSV1.1 TLSV1.2;

    ssl_dhparam         /etc/nginx/dhparam.pem;
```

ssl_dhparam         /etc/nginx/dhparam.pem;

Tool: [an online tester](https://www.ssllabs.com/ssltest/index.html)

# Issue certificates with Let's Encrypt

Prosody documents:

[Certificates](https://prosody.im/doc/certificates)

[using Let’s Encrypt with Prosody](https://prosody.im/doc/letsencrypt)
