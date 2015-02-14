'''
Created on Nov 1, 2014

@author: hyphen
'''
import random
import time
import Queue
from multiprocessing.managers import BaseManager

task_queue=Queue.Queue()
result_queue=Queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue',callable=lambda :task_queue)
QueueManager.register('get_result_queue',callable=lambda :result_queue)

manager=QueueManager(address=('',8888),authkey='ha')
manager.start()

task=manager.get_task_queue()
result=manager.get_result_queue()

for i in range(10):
    n=random.randint(0,10000)
    print('sending task %d....'%n)
    task.put(n)


print('attempt to receive messages......')

for i in range(10):
    r=result.get(timeout=10)
    print('receive:%s'%r)

print("receive all data from worker")
manager.shutdown()
