# server.py

# Lab 1
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
        #self._host = socket.gethostbyname(socket.gethostname())
        self._host = "192.168.122.203"
        print("HOST IP: {}".format(self._host))

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
            connection_socket, addr = self._socket.accept()
            print("Connected {}:{}".format( addr[0],addr[1] ))
            request = connection_socket.recv(1024)
            print "Request {}".format(request)

            try:
                filename = request.split()[1]
                outputmessage = ""
                print("FILENAME REQUESTED: {}".format(filename))
                f = open(filename[1:])
                connection_socket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

                for line in f:
                     outputmessage += line

                print "SENDING:\n--------------------------------------------------------------------------------\n{}".format(outputmessage)
                connection_socket.send(outputmessage.encode())
                connection_socket.send("\r\n\r\n".encode())
                print "--------------------------------------------------------------------------------\n"
                connection_socket.close()

                print("")

            except IOError:
                print "IOError: Cannot open file {}".format(filename)
                connection_socket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
                connection_socket.close()

            except IndexError as e:
                print "IndexError: {}".format(e)
                connection_socket.send("HTTP/1.1 500 Internal Server Error\r\n\r\n".encode())
                connection_socket.close()

            except Exception as e:
                print "Unknown exception: {}".format(e)

if __name__ == "__main__":
    s = Server()
    print("tcpserver.py started from command line")
    s.listen()
