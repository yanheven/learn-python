__author__ = 'hyphen'
import socket
import select
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',8888))
sock.listen(5)

ins=[sock]
ous=[]
data={}
adrs={}

try:
    while True:
        i,o,e=select.select(ins,ous,[])
        for x in i:
            if x is sock:
                newSocket,address=sock.accept()
                print "Connectd from:",address
                ins.append(newSocket)
                adrs[newSocket]=address
            else:
                newData=x.recv(8192)
                if newData:
                    print("%d bytes from %s"%(len(newData),adrs[x]))
                    data[x]=data.get(x,'')+newData
                    if x not in ous:
                        ous.append(x)
except Exception as e:
    print('%s' % e)
