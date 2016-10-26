import socket
import sys
import numpy as np
import cv2
import sys
import RPi.GPIO as GPIO
import time
import serial


##PWM y IO de la Raspberry##
Led=14;
GPIO.setwarnings(False);
GPIO.setmode(GPIO.BCM)
GPIO.setup(Led, GPIO.OUT,initial=GPIO.LOW)
#GPIO.setup(15, GPIO.IN)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
#print(sys.stderr, 'starting up on %s port %s', server_address)
sock.bind(server_address)

sock.listen(1)
conn, c_add = sock.accept()
print("conexión de: ",c_add)

while True:
    data = conn.recv(16)
    print("Se recibe: ",repr(data))
    rep = input("Responder: ")
    reply=str.encode(rep)
    conn.sendall(reply)


for i in range(0,10):
	GPIO.output(Led, GPIO.HIGH);
	time.sleep(0.1);
	GPIO.output(Led, GPIO.LOW);
	time.sleep(0.1);
