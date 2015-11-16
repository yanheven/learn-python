from pecan import expose, redirect, request, abort
from webob.exc import status_map
import pecan
import json
import time

from test_project.login import get_user

# pecan.route()

# # example:bookstore
# class BooksController(object):
#     @expose()
#     def index(self):
#         return "Welcome to book section."
#
#     @expose()
#     def bestsellers(self):
#         return "We have 5 books in the top 10."
#
# class CatalogController(object):
#     @expose()
#     def index(self):
#         return "Welcome to the catalog."
#
#     books = BooksController()
#
# class RootController(object):
#     @expose()
#     def index(self):
#         return "Welcome to store.example.com!"
#
#     @expose()
#     def hours(self):
#         return "Open 24/7 on the web."
#
#     catalog = CatalogController()


# # example:request content type
# class RootController(object):
#     @expose('json')
#     @expose('text_template.mako', content_type='text/plain')
#     @expose('html_template.mako')
#     def hello(self):
#         return {'msg': 'Hello!'}

# # example: path segment
# class RootController(object):
#
#     @pecan.expose(route='some-path')
#     def some_path(self):
#         return dict()
#
# use route method
# class RootController(object):
#
#     @pecan.expose()
#     def some_path(self):
#         return dict()
#
# pecan.route('some-path', RootController.some_path)

# class RootController(object):
#
#     @expose(generic=True, template='index.html')
#     def index(self):
#         return dict()
#
#     @index.when(method='POST')
#     def index_post(self, q):
#         redirect('http://pecan.readthedocs.org/en/latest/search.html?q=%s' % q)
#
#     @expose('error.html')
#     def error(self, status):
#         try:
#             status = int(status)
#         except ValueError:  # pragma: no cover
#             status = 500
#         message = getattr(status_map.get(status), 'explanation', '')
#         return dict(status=status, message=message)

# class UsersController(object):
#     @expose()
#     def index(self):
#         return 'hello user'
#
#     @expose('json')
#     def current_user(self):
#         '''
#         return an instance of myproject.model.User which represents
#         the current authenticated user
#         '''
#         # return 'hello current user'
#         # return "{'a':3}"
#         # print(json.dumps({'a':1}))
#         user = get_user.get_current_user()
#         print(user)
#         return user
#
#
# class RootController(object):
#     @expose()
#     def index(self, arg):
#         return arg
#
#     @expose()
#     def kwargs(self, **kwargs):
#         return str(kwargs)
# #
#     user = UsersController()

# or pecan.route(RootController, 'user', UsersController)

# # Note: this is *not* thread-safe.  In real life, use a persistent data store.
BOOKS = {
    '0': 'The Last of the Mohicans',
    '1': 'Catch-22'}
#
#
# class BookController(object):
#
#     def __init__(self, id_):
#         self.id_ = id_
#         assert self.book
#
#     @property
#     def book(self):
#         if self.id_ in BOOKS:
#             return dict(id=self.id_, name=BOOKS[self.id_])
#         abort(404)
#
#     # HTTP GET /<id>/
#     @expose(generic=True, template='json')
#     def index(self):
#         return self.book
#
#     # HTTP PUT /<id>/
#     @index.when(method='PUT', template='json')
#     def index_PUT(self, **kw):
#         BOOKS[self.id_] = kw['name']
#         return self.book
#
#     # HTTP DELETE /<id>/
#     @index.when(method='DELETE', template='json')
#     def index_DELETE(self):
#         del BOOKS[self.id_]
#         return dict()
#
#
from pecan import expose
from pecan.rest import RestController

from test_project.model import User

# class BooksController(RestController):
#
#     def __init__(self, id_):
#         self.id_ = id_
#         assert self.book
#
#     @property
#     def book(self):
#         if self.id_ in BOOKS:
#             return dict(id=self.id_, name=BOOKS[self.id_])
#         abort(404)
#
#     _custom_actions = {
#         'checkout':['DELETE']
#     }
#
#     @expose(template='json')
#     def get(self, id_):
#         # import pdb
#         # pdb.set_trace()
#         # return {"1":"a"}
#         # name = BOOKS.get(id)
#         # return {id:name}
#
#         book = BOOKS.get(id_)
#         if not book:
#             abort(404)
#         return {id_:book}
#
#     @expose(template='json')
#     def checkout(self,id_):
#         del BOOKS[id_]
#         return dict()

class BooksController(object):

    def __init__(self, id):
        self.id = id
    #     assert self.book
    #
    # @property
    # def book(self):
    #     if self.id in BOOKS:
    #         return dict(id=self.id, name=BOOKS[self.id])
    #     abort(404)

    @expose(generic=True, template='json')
    def index(self):
        return {'a':'1'}
        # return {self.id:self.book}


class RootController(object):
    #
    @expose()
    def _lookup(self, id, *remainder):
        return BooksController(id), remainder
    # HTTP GET /

    @expose(generic=True, template='json')
    def index(self):
        time.sleep(10)
        return [dict(id=k, name=v) for k, v in BOOKS.items()]

    # HTTP POST /
    @index.when(method='POST', template='json')
    def index_POST(self, **kw):
        id_ = len(BOOKS)
        BOOKS[id_] = kw['name']
        return dict(id=id_, name=kw['name'])

    # book = BooksController()
