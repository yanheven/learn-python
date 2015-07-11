'''
Created on Nov 23, 2014

@author: hyphen
'''
import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import urllib2
import simplejson as json
import time

start=time.time()
tic=lambda:"at %1.1f"%(time.time()-start)

def fetch(pid):
    response=urllib2.urlopen("http://www.baidu.com")
    result=response.read()
    #print result
    #json_result=json.load(result)
    #datetime=json_result['datetime']
    #gevent.sleep(0.1)
    datetime=tic
    print("task %s:%s"%(pid,datetime()))
    
def synchronous():
    for i in range(10):
        fetch(i)
        
def asynchronous():
    threads=[]
    for i in range(10):
        threads.append(gevent.spawn(fetch,i))
    gevent.joinall(threads)
    
print("synchronous:")
synchronous()

print("asynchronous:")
asynchronous()
    