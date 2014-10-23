__author__ = 'hyphen'
from multiprocessing import Process
import os
def run_child(name):
    print('child process %s fork from %s'%(name,os.getppid()))

if __name__=='__main__':
    print('parent process %s'%os.getpid())
    p=Process(target=run_child,args=('test',))
    print('Process start')
    p.start()
    p.join()
    print('Process stop')