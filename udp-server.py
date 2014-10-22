__author__ = 'hyphen'
import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('',8889))

try:
    while True:
        data,address=sock.recvfrom(8192)
        print "Datagram from",address,data
        sock.sendto(data,address)

finally:
    sock.close()