import numpy as np
import cv2
import sys
import argparse
import imutils

cap = cv2.VideoCapture(0)
upper = np.array([0, 255, 0])
lower = np.array([0, 0, 200])

#black_upper = (110,110,95)
#black_lower = (90,90,70)

#HSV hue sat value

black_upper = (100, 0, 0)
black_lower = (0, 0, 0)

while(True):
	ret, frame = cap.read()
	#frame = imutils.resize(frame, width=600)
	if ret == True:
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		
	mask = cv2.inRange(hsv,black_lower,black_upper)
	
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	center=None
	
	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
 
 		if radius > 1:
			cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
			#org = cv2.FONT_HERSHEY_SIMPLEX
			#cv2.putText(frame,'Javier',center,org,1,(255,255,255),2,cv2.LINE_AA);
	
		 
	# draw a green bounding box surrounding the red game
	#for (x, y, w, h) in cnts:
    #       cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	#cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)
	cv2.imshow('Frame',frame)
	cv2.imshow('mask',mask)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
