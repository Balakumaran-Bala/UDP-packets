import socket
import sys
from threading import Thread

UDP_IP_ADDRESS = "10.0.0.133"
UDP_PORT_NO = 6789

MAC_ADDRESS = "10.0.0.210"
MAC_PORT = 7891

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#clientSocket_receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
#clientSocket_receive.bind((MAC_PORT, MAC_PORT))

def receive():
	while True:
		data = clientSocket.recv(1024)

		print "\n" + data

t = Thread(target=receive)
t.start()

while True:
	Message = raw_input("Message: ")
	clientSocket.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
	

