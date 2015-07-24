# /var/www/simpleapp/app.wsgi
from pecan.deploy import deploy
application = deploy('/home/evan/code/yanheven/learn-python/learn_pecan/test_project/config.py')
