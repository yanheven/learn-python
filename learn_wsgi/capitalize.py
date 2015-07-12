__author__ = 'evan'
from webob import Request

# class Capitalizer(object):
#
#     # We generally pass in the application to be wrapped to
#     # the middleware constructor:
#     def __init__(self, wrap_app):
#         self.wrap_app = wrap_app
#
#     def __call__(self, environ, start_response):
#         # We call the application we are wrapping with the
#         # same arguments we get...
#         response_iter = self.wrap_app(environ, start_response)
#         # then change the response...
#         response_string = ''.join(response_iter)
#         return [response_string.upper()]

class Capitalizer(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        req = Request(environ)
        resp = req.get_response(self.app)
        resp.body = resp.body.upper()
        return resp(environ, start_response)