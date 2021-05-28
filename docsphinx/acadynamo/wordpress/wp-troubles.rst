Troubleshootings
================

.. _trouble-compose-mysql:

1. Setup db for composed image

.. image:: ../imgs/09-wp-compose-db.png

If it report trouble, first check your network::

    docker network ls

Then inspect the network

::

    # 'wordpress' is the image name showed above
    docker network inspact wordpress

Here is an example causing trouble::

    [{
        "Name": "wordpress_default",
        "Id": "bd7d0b083d606aaf20b5bceff725093e423d74fce0a79938040b600c53c4a48d",
        "Created": "2021-05-27T14:25:08.4686924Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {},
        "Options": {},
        "Labels": {
            "com.docker.compose.network": "default",
            "com.docker.compose.project": "wordpress",
            "com.docker.compose.version": "1.0-alpha"
        }
    }]

This is probably you start up docker container with 'run' command, letting mysql
container not up.

Here is the correct one (mysql is up)::

    [ {
        "Name": "wordpress_default",
        "Id": "bd7d0b083d606aaf20b5bceff725093e423d74fce0a79938040b600c53c4a48d",
        "Created": "2021-05-27T14:25:08.4686924Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "0e19d4e70498787f1ccddcffe2ca95555cadb38232a7bb15be5d723c8e427a61": {
                "Name": "wordpress_web_1",
                "EndpointID": "24aa719fbde99637985315a4eb34affa9db3fda729c2b5a7a1896a87f461a0b0",
                "MacAddress": "##:##:##:##:##:##",
                "IPv4Address": "172.18.0.3/16",
                "IPv6Address": ""
            },
            "179c9e5625bc976b14ea4800f8c684124e7b44301b1686958b470bc981ef75e6": {
                "Name": "wordpress_mysql_1",
                "EndpointID": "50cc01a08ef6b54c444c01f7716aa8df6e598ef2bdb02694d57e7ea4ad6be8a4",
                "MacAddress": "##:##:##:##:##:##",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {
            "com.docker.compose.network": "default",
            "com.docker.compose.project": "wordpress",
            "com.docker.compose.version": "1.0-alpha"
        }
    } ]
