import numpy as np
import cv2
import sys
import RPi.GPIO as GPIO
import time
import socket
import sys
import numpy as np
import sys
import RPi.GPIO as GPIO
import time
import serial

##PWM y IO de la Raspberry##

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14, GPIO.OUT)
pwm_o = GPIO.PWM(14, 50)
pwm_o.start(7.5)
time.sleep(0.005)
for ang in range(1,181,1):
        ang=float(ang)
        duty=float((ang/180))*9.5 + 2.5
        pwm_o.ChangeDutyCycle(duty)
        time.sleep(0.005)
print('/n')
print('Porton Abierto')
pwm_o.ChangeDutyCycle(7.5)
time.sleep(0.005)
pwm_o.stop()
GPIO.cleanup()

