__author__ = 'evan'
from objectpub import ObjectPublisher
from auth import AuthMiddleware
from capitalize import Capitalizer

class Root(object):

    def __call__(self):
        return '''
            <form  action="welcome">
            Name: <input type="text" name="name">
            <input type="submit">
            </form>
                '''

    def welcome(self, name):
        return 'Hello %s' % name

app = ObjectPublisher(Root())
auth_app = AuthMiddleware(app)
# capital_app = Capitalizer(auth_app)
# from paste.exceptions.errormiddleware import ErrorMiddleware
# exc_wrapped_app = ErrorMiddleware(auth_app)

from paste.evalexception import EvalException
exc_wrapped_app = EvalException(auth_app)

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(exc_wrapped_app, host='0.0.0.0', port='8080')