__author__ = 'hyphen'
import time,threading

def loop():
    print('thread %s start'%threading.current_thread().name)
    for i in range(5):
        print('now is %s'%threading.current_thread().name)
        time.sleep(1)
    print('some one is ended %s'%threading.current_thread().name)

print('thread %s runing..'%threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('who %s ended'%threading.current_thread().name)
