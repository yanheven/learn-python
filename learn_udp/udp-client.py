__author__ = 'hyphen'
import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data="""this is just
a test writen by
hyphen to test udp
connection."""

for line in data.splitlines():
    sock.sendto(line,('localhost',8889))
    print("Sent : "+line)
    response=sock.recv(8192)
    print("Received: "+response)

sock.close()