import argparse
import sys
import os
import re

from urllib.parse import urlparse, parse_qs

from http.server import test, SimpleHTTPRequestHandler, HTTPServer

class AnHttpRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        '''
        Thanks to https://stackoverflow.com/a/8930440/7362888

        note: self.path is the url sub-path. 
        '''
        qs = parse_qs(urlparse(self.path).query);
        self.shutdownFlag = qs.get('_shut-down_', [''])

        # replace nonce (getNonce()) with nonce (should be *.html)
        nonce = qs.get('nonce')
        if nonce and len(nonce[0]) > 0:
            self.path = re.sub(r'\w{10,}.html', nonce[0] + '.html', self.path)
            self.path = re.sub(r'\w{10,}.py', nonce[0] + '.py', self.path)
            self.path = re.sub(r'\w{10,}.tier', nonce[0] + '.tier', self.path)
            self.path = re.sub(r'\w{10,}.less', nonce[0] + '.less', self.path)
        print(self.path);
        
        # print(self.shutdownFlag, self.shutdownFlag[0] == 'True')
        super(type(self), self).do_GET()
        if self.shutdownFlag[0] == 'True':
            raise KeyboardInterrupt
        
class AnHTTPServer(HTTPServer):

    def _handle_request_noblock(self):
        try:
            request, client_address = self.get_request()
        except OSError:
            return
        if self.verify_request(request, client_address):
            try:
                self.process_request(request, client_address)
            except KeyboardInterrupt:
                print('Shutting down on client requests ...')
                raise KeyboardInterrupt
            except:
                self.handle_error(request, client_address)
                self.shutdown_request(request)
        else:
            self.shutdown_request(request)
         
        print(client_address)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--cgi', action='store_true',
                       help='Run as CGI Server')
    parser.add_argument('--bind', '-b', default='', metavar='ADDRESS',
                        help='Specify alternate bind address '
                             '[default: all interfaces]')
    parser.add_argument('port', action='store',
                        default=8888, type=int,
                        nargs='?',
                        help='Specify alternate port [default: 8888]')

    parser.add_argument('--webroot', '-w', default='',
                        help = 'Specify the web root directory ~ v3.7 directory')
    args = parser.parse_args()

    print("webroot:", args.webroot)
    os.chdir(args.webroot)
    
    if args.cgi:
        handler_class = CGIHTTPRequestHandler
    else:
        handler_class = AnHttpRequestHandler # SimpleHTTPRequestHandler

    test(HandlerClass=handler_class, ServerClass=AnHTTPServer, port=args.port, bind=args.bind)
