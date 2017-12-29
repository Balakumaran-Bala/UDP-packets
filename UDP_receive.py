import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

UDP_IP_ADDRESS = "10.0.0.133"
UDP_PORT_NO = 6789
MAC_ADDRESS = "10.0.0.210"
MAC_PORT = 7891

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

while True:
    data, addr = serverSock.recvfrom(1024)
    print "Message: ", data
    if data == "on":
        print "LED on"
        GPIO.output(18, GPIO.HIGH)
        serverSock.sendto("ON", (MAC_ADDRESS, UDP_PORT_NO))
        time.sleep(3)
    elif data == "off":
        print "LED off"
        GPIO.output(18, GPIO.LOW)
        serverSock.sendto("OFF", (MAC_ADDRESS, UDP_PORT_NO))
        time.sleep(3)
