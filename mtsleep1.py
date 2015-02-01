__author__ = 'hyphen'
import thread
from time import sleep,ctime

def loop1():
    print('sart loop1 at :%s'%ctime())
    sleep(4)
    print('loop 1 done at :%s'%ctime())

def loop2():
    print('sart loop2 at :%s'%ctime())
    sleep(2)
    print('loop 2 done at :%s'%ctime())

if __name__ == '__main__':
    print('start at %s'%ctime())
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2,())
    sleep(6)
    print('all done at %s'%ctime())