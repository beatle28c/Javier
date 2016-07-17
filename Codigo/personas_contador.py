import numpy as np
import cv2
import sys
import argparse
import imutils

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = True) 

while(True):
	ret, frame = cap.read()
	if ret == True:
		gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	fgmask = fgbg.apply(frame)
	try:
		cv2.imshow('frame',frame)
		cv2.imshow('Background Substraction',fgmask)
	except:
		print('EOF')
		break   
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
