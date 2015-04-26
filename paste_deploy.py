__author__ = 'hyphen'
from paste.deploy import loadapp
wsgi_app=loadapp('config:paste.ini')