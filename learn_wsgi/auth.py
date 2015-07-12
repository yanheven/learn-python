__author__ = 'evan'
from webob import Request, Response

class AuthMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        req = Request(environ)
        # print req
        # import pdb
        # pdb.set_trace()
        if not self.authorized(req.headers.get('authorization')):
            resp = self.auth_required(req)
        else:
            resp = self.app
        return resp(environ, start_response)

    def authorized(self, header):
        if not header:
            return False
        auth_type, encoded = header.split(None, 1)
        if not auth_type.lower() == 'basic':
            return False
        username, password = encoded.decode('base64').split(':', 1)
        return self.check_password(username, password)

    def check_password(self, username, password):
         return username == password

    def auth_required(self, req):
         return Response(status=401, headers={'WWW-Authenticate': 'Basic realm="this realm"'},
                         body="""\
         <html>
          <head><title>Authentication Required</title></head>
          <body>
           <h1>Authentication Required</h1>
           If you can't get in, then stay out.
          </body>
         </html>""")