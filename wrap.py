__author__ = 'hyphen'
import functools

def log(test):
    def decarator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print 'begin %s'%test
            func(*args,**kw)
            print "end call"
        return wrapper
    return decarator


@log('oo')
def f():
    print "hello"

