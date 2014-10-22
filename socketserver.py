__author__ = 'hyphen'
import SocketServer
class EchoHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print "Connected from:",self.client_address
        while True:
            receivedData=self.request.recv(8192)
            if not receivedData:
                break
            self.request.sendall(receivedData)
        self.request.close()
        print "Disconnected from:",self.client_address

srv=SocketServer.ThreadingTCPServer(('',8888),EchoHandler)
srv.serve_forever()