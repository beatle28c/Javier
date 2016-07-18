import numpy as np
import cv2
import sys
import RPi.GPIO as GPIO
import time

cara = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
wcam=cam.get(3)
hcam=cam.get(4)
mw = int(wcam/2) #
mh = int(hcam/2) #

a1=0
b1=mh
a2=2*mw
b2=mh
cuenta=0
minLineLength = 100
maxLineGap = 10

##PWM y IO de la Raspberry##
ang=input("Valor PWM")
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)


while True:
	
	pwm = GPIO.PWM(14, 100)
	pwm.start(ang)
    
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()
