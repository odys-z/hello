# This Python file uses the following encoding: utf-8

import requests

url = 'http://192.168.0.145:8964/jserv-album/login.serv'
myobj = {
"type": "io.odysz.semantic.jprotocol.AnsonMsg",
"version": "1.0", "seq": 966, "port": "session",
"header": {"type":"io.odysz.semantic.jprotocol.AnsonHeader"},
"body":[{
    "type":"io.odysz.semantic.jsession.AnSessionReq",
    "a":"login",
    "parent":"io.odysz.semantic.jprotocol.AnsonMsg",
    "uri":"/album/sys",
    "uid":"ody",
    "token":"ZB80XpH0mXh8DS2897rZ4A==",
    "iv":"FwEfCVgMYDhEGgpODRkFWQ=="}]
}


class Anclient:
    def __init__(self):
        pass

    def ping(self):
        x = requests.post(url, json = myobj)
        print(x)
