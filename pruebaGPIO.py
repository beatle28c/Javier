#!/usr/bin/env python
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

for i in range(0,10):
	GPIO.output(Led, GPIO.HIGH);
	time.sleep(0.1);
	GPIO.output(Led, GPIO.LOW);
	time.sleep(0.1);
