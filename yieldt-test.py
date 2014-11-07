__author__ = 'hyphen'
def foo():
    for i in range(10):
        yield i
        print 'foo:here '+str(i)

bar=foo()

print(bar.next())
print("main:here")
print(bar.next())
print(bar.next())
print(list(foo()))