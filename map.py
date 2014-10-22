__author__ = 'hyphen'
def f(x):
    return x**2

#print map(f,[1,2,3,4,5])

def add(a,b):
    return a+b

#print reduce(add,[1,2,3,4,5])

def parseten(x,y):
    return x*10+y


#print reduce(parseten,[1122334])

def str2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

#print type(reduce(parseten,map(str2num,'2333432')))

def my_map(fn,*args):
    newlist=[]
    for i in args:
        newlist.append(fn(i))
    return newlist

#print my_map(f,12,23,34,45,56)

def prob(l):
    def multiple(a,b):
        return a*b
    return reduce(multiple,l)

#print prob([1,2,3,4,5])

f=lambda x:x**2
print f


