__author__ = 'hyphen'
import socket
for i in range(10):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('localhost',8888))
    print("Connected to server")
    data="""A few lines of data
    to test the operation
    of both server and client."""

    for line in data.splitlines():
        sock.sendall(line)
        print("Sent :"+line)
        response=sock.recv(8192)
        print("Received : "+response)

    sock.close()