import numpy as np
import cv2
import sys
import RPi.GPIO as GPIO
import time
import serial


##PWM y IO de la Raspberry##
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(15, GPIO.IN)


ser = serial.Serial('/dev/ttyUSB0', 9600)
string = 'Hello from Raspberry Pi'
print 'Sending "%s"' % string
ser.write('%s\n' % string)

while True:
	incoming = ser.readline().strip()
	print 'Received %s' % incoming
	ser.write('RPi Received: %s\n' % incoming)

#while True:	
#	cond=GPIO.input(15);
#	if cond==True:
#		led = GPIO.output(14, GPIO.HIGH)
#	else:
#		led = GPIO.output(14, GPIO.LOW)
