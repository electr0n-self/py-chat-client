#! /usr/local/bin/python

from socket import *
import time


HOST = '127.0.0.1'
PORT = 21567
ADDR = (HOST, PORT)
BUFFSIZE = 1024


client_socket = socket(AF_INET, SOCK_STREAM);
client_socket.connect(ADDR);
#ans = client_socket.recv(BUFFSIZE);
#print ans;
while True:
	msg = raw_input("> ");
	client_socket.send(msg);
	ans = client_socket.recv(BUFFSIZE);
	print ans;
client_socket.close();
