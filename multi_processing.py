__author__ = 'hyphen'
import os

print('process %s start..../.'%os.getpid())
pid=os.fork()
if pid==0:
    print('child process %s fork frok from %s'%(os.getpid(),os.getppid()))
else:
    print('parent %s create a process %s'%(os.getpid(),pid))