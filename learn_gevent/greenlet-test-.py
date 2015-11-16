__author__ = 'hyphen'
from greenlet import greenlet

def t1():
    print 1
    gr2.switch()
    print 2

def t2():
    print 3
    gr1.switch()
    print 4

gr1=greenlet(t1)
gr2=greenlet(t2)
gr1.switch()