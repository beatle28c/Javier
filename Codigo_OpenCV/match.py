import numpy as np
import cv2
import sys
import argparse
import imutils
 
image = cv2.imread('puertos.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread('puerto.jpg',0)
w,h = template.shape[::-1]

res = cv2.matchTemplate(image_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
font=cv2.FONT_HERSHEY_SIMPLEX
n = 0
for pt in zip(*loc[::-1]):
	n = n+1
	number=str(n)
	cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
	cv2.putText(image,number,(pt[0] + w, pt[1] + h), font, 1, (200,255,155), 1, cv2.LINE_AA)

cv2.imshow('Detected',image)
cv2.waitKey(0)
