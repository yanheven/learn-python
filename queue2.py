__author__ = 'hyphen'
import time,sys,Queue
from multiprocessing.managers import  BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr='0.0.0.0'
print('connecting to server %s......'%server_addr)

m=QueueManager(address=(server_addr,8888),authkey='ha')
m.connect()

task=m.get_task_queue()
result=m.get_result_queue()

for i in range(10):
    try:
        n=task.get(timeout=1)
        print('get data %d + %d from server'%(n,n))
        r='%d + %d = %d'%(n,n,n+n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print("server is empty")

print('worker quit')
