import numpy as np
import cv2
import sys
import RPi.GPIO as GPIO
import time
import serial
import socket
import ethernet

app = flas(_name_);


##IO de la Raspberry##
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT,initial=GPIO.LOW)

host_name = socket.gethostname();
host_ip = socket.get.hostbyname(host_name);
print(
