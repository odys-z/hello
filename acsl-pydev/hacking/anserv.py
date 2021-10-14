# import html
# import http.client
# import io
# import mimetypes
# import os
# import posixpath
# import select
# import shutil
# import socket # For gethostbyaddr()
# import socketserver
# import sys
# import time
# import urllib.parse
# import copy
import argparse

from urllib.parse import urlparse, parse_qs

# from http import HTTPStatus

from http.server import test, SimpleHTTPRequestHandler

class AnHttpRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        '''
        Thanks to https://stackoverflow.com/a/8930440/7362888
        '''
        # super.do_GET()
        self.shutdownFlag = parse_qs(urlparse(self.path).query).get('_shut-down_', [''])
        print(self.shutdownFlag, self.shutdownFlag[0] == 'True')
        super(type(self), self).do_GET()
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--cgi', action='store_true',
                       help='Run as CGI Server')
    parser.add_argument('--bind', '-b', default='', metavar='ADDRESS',
                        help='Specify alternate bind address '
                             '[default: all interfaces]')
    parser.add_argument('port', action='store',
                        default=8000, type=int,
                        nargs='?',
                        help='Specify alternate port [default: 8000]')
    args = parser.parse_args()
    if args.cgi:
        pass # handler_class = CGIHTTPRequestHandler
    else:
        handler_class = AnHttpRequestHandler # SimpleHTTPRequestHandler
    test(HandlerClass=handler_class, port=args.port, bind=args.bind)
