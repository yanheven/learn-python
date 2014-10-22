__author__ = 'hyphen'
import BaseHTTPServer

class TrivialHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """Trivial http request handler,answers not found to every request"""
    server_version = "TrivialHTTP/1.0"
    def do_GET(self):
        """serve a get reqtest."""
        self.send_error(404,"file not found,haha mengqi")
    do_HEAD=do_POST=do_GET

server=BaseHTTPServer.HTTPServer(('',80),TrivialHTTPRequestHandler)
server.serve_forever()