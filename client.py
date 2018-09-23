# client.py

# Lab 1
# CSC 361 - UVIC - Fall 2018
# Prof. Mantis CHENG
# Student: Alex L. DEWEERT
# ID: V00855767

import socket
import sys

class Client:

    def __init__(self, *args):

        try:
            self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._args_ip = args[0][1]
            self._args_port = args[0][2]
            self._args_filename = args[0][3]
            print( "CLIENT ARGS [ip]: {} [port]: {} [filename]: {}".format(self._args_ip,self._args_port,self._args_filename) )

        except socket.error:
            print "Error. Could not create socket"
            sys.exit()

    def run(self):
        try:
            message = "GET /{} HTTP/1.1".format(self._args_filename)
            self._s.connect((self._args_ip , int(self._args_port)))
            self._s.sendall(message)
        except socket.error as e:
            print "Send failed: {}".format(e)
            sys.exit()

        while(True):
            reply = self._s.recv(4096)
            if not reply: break
            print "Reply from server: {}".format(reply)

if __name__ == "__main__":
    client = Client(sys.argv)
    client.run()
