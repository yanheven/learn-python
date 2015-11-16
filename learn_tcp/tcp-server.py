__author__ = 'hyphen'
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8888))
sock.listen(5)

try:
    while True:
        newSocket, address = sock.accept()
        print "Connect from ", address
        while True:
            receiveData = newSocket.recv(8192)
            if not receiveData:
                break
            newSocket.sendall(receiveData)
        newSocket.close()
        print "Disconnect from ", address
# except Exception as e:
#     print('%s' % e)
finally:
    sock.close()