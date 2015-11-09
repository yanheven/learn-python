__author__ = 'evan'
from openstack import connection

conn = connection.Connection(auth_url='http://localhost:5000/v2.0/',
                             project_name='demo',
                             username='admin',
                             password='nomoresecrete')
actionBody = {'reboot':{'type':'SOFT'}}
servers = conn.compute.servers(details=False, name='p')
for server in servers:
    print server
    # server.action(session=conn.session,body=actionBody)
    #server.action(session=conn.session,body={'os-stop':None})
    server.action(session=conn.session,body={'os-stop':None})