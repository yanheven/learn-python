__author__ = 'hyphen'

def updaown(N):
    for x in range(1,N):yield x
    for x in range(N,0,-1):yield x


if __name__=="__main__":
    # print xrange(1,4)
    for i in updaown(5):print(i)