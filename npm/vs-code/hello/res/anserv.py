import argparse
import sys
import os

from urllib.parse import urlparse, parse_qs

from http.server import test, SimpleHTTPRequestHandler, HTTPServer

class AnHttpRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        '''
        Thanks to https://stackoverflow.com/a/8930440/7362888
        '''
        self.shutdownFlag = parse_qs(urlparse(self.path).query).get('_shut-down_', [''])
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
