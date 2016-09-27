import numpy as np
import cv2
import sys
import RPi.GPIO as GPIO
import time

a1=0
b1=mh
a2=2*mw
b2=mh
cuenta=0
minLineLength = 100
maxLineGap = 10

##PWM y IO de la Raspberry##
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT,initial=GPIO.low)
GPIO.setup(15, GPIO.IN)

while True:
	
	cond=GPIO.input(15);
	if cond==TRUE:
		led = GPIO.output(14, GPIO.HIGH)
	else:
		led = GPIO.output(14, GPIO.LOW)
