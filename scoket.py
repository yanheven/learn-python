__author__ = 'hyphen'
import socket

print socket.AF_INET
print(socket.AF_INET6)
for i in (socket.AF_INET,socket.AF_INET6):
    print(socket.inet_pton(i,"10.0.0.1"))