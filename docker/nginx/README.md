# Firewall @ Centos 7

[CentOS: Firewall settings](https://www.printsupportcenter.com/hc/en-us/articles/360000689849-CentOS-Firewall-settings)

```
    firewall-cmd --zone=public --list-all
    firewall-cmd --zone=public --add-port=443/tcp --permanent
    firewall-cmd --reload
```

# Issue certificates with Let's Encrypt

Install snapd, certbot on CentOS,
see [certbot instructions](https://certbot.eff.org/lets-encrypt/centosrhel7-other).

Issue cert while nginx stopped:

```
    sudo certbot certonly --standalone
```

Generating Diffie-Hellman Ephemeral algorithm parameters (Not sure?) :

```
    openssl dhparam -out /etc/nginx/dhparam.pem
```

# Turn on SSL

[Issue certs with Let's Encrypt Certbot standalone]()

```
    ssl_certificate "/etc/letsencrypt/live/domain.com/fullchain.pem";
    ssl_certificate_key "/etc/letsencrypt/live/domain.com/privkey.pem";
    ssl_protocols TLSV1.1 TLSV1.2;

    ssl_dhparam         /etc/nginx/dhparam.pem;
```

# Extend certificate expiration

```
    certbot
```

then select the domain.
