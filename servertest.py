# server.py

# Lab1
# CSC 361 - UVIC - Fall 2018
# Prof. Mantis CHENG
# Student: Alex L. DEWEERT
# ID: V00855767

import socket
import sys
import threading

class Server:


    def __init__(self):
        self._port = 8888
        self._host = "134.87.162.240"

        try:
            self._socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            print("Created socket object...")
        except socket.error, msg:
            print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()

        try:
            self._socket.bind( (self._host, self._port) )
            print("...Socket object bound successfully")
        except socket.error, msg:
            print 'Failed to bind socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()


    def listen(self):
        self._socket.listen(5);
        print("Listening on port: ", self._port)
        while 1:
            client_sock, addr = self._socket.accept()
            print("Connected {}:{}".format( addr[0],addr[1] ))
            client_handler = threading.Thread(
                target=self.handleConnection,
                args=(client_sock,))
            client_handler.start()

    def handleConnection(self, client_sock):
        request = client_sock.recv(1024)
        print "Received {}".format(request)
        client_sock.send("Server success response to {}".format(request))
        client_sock.close()


if __name__ == "__main__":
    s = Server()
    print("tcpserver.py started from command line")
    s.listen()
