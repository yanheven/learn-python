'''
Created on Nov 7, 2014

@author: hyphen
'''
from wsgiref.simple_server import make_server
from hello import  application
httpd=make_server('',8000,application)
print('server listen on port 8000...')

httpd.serve_forever()
