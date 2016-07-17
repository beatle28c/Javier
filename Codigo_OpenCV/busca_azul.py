import numpy as np
import cv2
import sys
import argparse
import imutils

cap = cv2.VideoCapture(0)
black_upper = np.array([140,255,255])
black_lower = np.array([110, 50, 50])

while(True):
	ret, frame = cap.read()
	#frame = imutils.resize(frame, width=600)
	if ret == True:
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		
	mask = cv2.inRange(hsv,black_lower,black_upper)
	res=cv2.bitwise_and(frame,frame,mask=mask)
	#bilateral=cv2.bilateralFilter(res,15,75,75)
	
	
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	c = max(cnts, key=cv2.contourArea)
	
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.05 * peri, True)
	cv2.drawContours(frame, [approx], -1, (0, 255, 0), 4)
	
	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	#cv2.imshow('bilateral',bilateral)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
