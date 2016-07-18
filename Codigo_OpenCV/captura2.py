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

black_upper = (95,110,110)
black_lower = (70,90,90)

#black_lower = (29, 86, 6)
#black_upper = (64, 255, 255)

x,y,w,h = 900,600,70,70
c,r,w,h = 900,600,70,70
track_window = (c,r,w,h)



while(True):
	ret, frame = cap.read()
	roi = frame[r:r+h, c:c+w]
	hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv_roi, (32,30,0), (255,255,180))
	roi_hist = cv2.calcHist(hsv_roi, [0], mask, 180, [0, 180])
	cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
	term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 80, 1)
	if ret == True:
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		dst = cv2.calcBackProject(hsv,0,roi_hist,[0,180],1)
		ret, track_window = cv2.meanShift(dst, track_window, term_crit)	
	cv2.rectangle(frame, (x,y), (x+w,y+h), 255, 2)
    #cv2.putText(frame, 'Tracked', (x,y), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)
	cv2.imshow('Video',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
