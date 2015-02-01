'''
Created on Nov 23, 2014

@author: hyphen
'''
import gevent
import random
import time

start=time.time()
tic=lambda:"at %1.1f"%(time.time()-start)
random_time=lambda:random.randint(0,2)*0.1

def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(random_time())
    print('Task %s done' % pid)

def synchronous():
    print("start synchronous %s:"%tic())
    for i in range(0,10):
        task(i)
    print("end synchronous %s:"%tic())

def asynchronous():
    print("start asynhronous :%s"%tic())
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)
    print("end asynchronous %s"%tic())

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()