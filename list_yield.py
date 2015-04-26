__author__ = 'heven'

def test_yield():
    for i in range(10):
        yield i

a =list(test_yield())
print a