import socket
import sys
from threading import Thread

UDP_IP_ADDRESS = "10.0.0.133"
UDP_PORT_NO = 6789

MAC_ADDRESS = "10.0.0.210"
MAC_PORT = 7891

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#clientSocket.bind((MAC_ADDRESS, MAC_PORT))

def recv():
	while True:
		data = clientSocket.recv(1024)
		if not data: sys.exit(0)
		print data

while True:
	Message = raw_input("Message: ")
	clientSocket.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
	Thread(target=recv).start()