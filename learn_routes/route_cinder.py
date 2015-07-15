#coding=utf-8
__author__ = 'evan'
#!/usr/bin/env/python
# http://blog.csdn.net/qiushanjushi/article/details/45098703
# http://routes.readthedocs.org/en/latest/restful.html

from routes import Mapper
map = Mapper()
map.connect(None,"error/{action}/{id}",controller="controller_obj") #定义匹配规则
result = map.match('error/myapp/4')  #匹配url='error/myapp/4'
#result 匹配结果
{'action': u'myapp', 'controller': u'controller_obj', 'id': u'4'}
map.connect(None,"/message/:name",controller='my_contro')  #除 {} 外，：也可以作为匹配符号
result = map.match('/message/12')
#result 匹配结果
{'controller': u'my_contro', 'name': u'12'}


from pprint import pprint
from routes import Mapper
from routes import middleware
import webob.dec
from wsgiref.simple_server import make_server

class controller(object):

    def __init__(self):
        self.i = 1

    def __call__(self):
        print self.i

    def search(self):
        return "do search()"

    def show(self):
        return "do show()"

    def index(self):
        return "do index()"

    def update(self):
        return "do update()"

    def delete(self):
        return "do delete()"

    def create(self):
        return "do create()"

    def create_many(self):
        return "do create_many()"

    def update_many(self):
        return "do update_many()"

    def list_many(self):
        return "do list_many()"

    def delete_many(self):
        return "do delete_many()"

class appclass(object):

    def __init__(self):
        a = controller()
        map = Mapper()
        """路由匹配条件1"""
        # map.connect('/images',controller=a,
        #           action='search',
        #           conditions={'method':['GET']})
        """路由匹配条件2"""
        #map.connect('name',"/{action}/{pid}",controller=a)
        """路由匹配条件3"""
        #map.resource("message","messages",controller=a,collection={'search':'GET'})
        """路由匹配条件4"""
        #map.resource('message', 'messages',controller=a,
                        #collection={'list_many':'GET','create_many':'POST'},
                        #member={'update_many':'POST','delete_many':'POST'})
        """路由匹配条件5"""
        map.resource('controller', 'controllers',controller=a,path_prefix='/{projectid}',
                    collection={'list_many':'GET','create_many':'POST'},
                    member={'update_many':'GET','delete_many':'POST'})
        # http://192.168.56.254:8088/1/controllers/list_many
        # http://192.168.56.254:8088/1/controllers/1/update_many

        self.route = middleware.RoutesMiddleware(self.dispatch,map)

    @webob.dec.wsgify
    def __call__(self,req):
        return self.route

    @staticmethod
    @webob.dec.wsgify
    def dispatch(req):
        match = req.environ['wsgiorg.routing_args'][1]
        print "route match result is:",match
        if not match:
            return "fake url"

        controller = match['controller']
        action = match['action']
        if hasattr(controller,action):
            func = getattr(controller,action)
            ret = func()
            return ret
        else:
            return "has no action:%s" %action


if __name__=="__main__":
    app = appclass()
    server = make_server('0.0.0.0',8088,app)
    server.serve_forever()
