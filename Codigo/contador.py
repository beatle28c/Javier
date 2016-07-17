import numpy as np
import cv2
import sys
import argparse
import imutils

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

while True:

    ret, frame = cam.read()

    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray,50,150,apertureSize = 3)
	
	faces = cara.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE
		)
		
	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		#cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		frame=cv2.line(frame,(x+(w/2), y), (x+(w/2), y+h),(255,0,0), 2, 8)
		frame=cv2.line(frame,(x, y+(h/2)), (x+w,y+(h/2)),(255,0,0), 2, 8)
		frame=cv2.circle(frame,(x+(w/2), y+(h/2)),(w/2),(0,0,255), 2, 8)
		a=(x+w/2)
		b=(y+h/2)
		center = (a,b)
		cv2.circle(frame, center, 5, (0, 0, 255), -1)
		if(b < mh+10 and b > mh-10):
			cuenta=cuenta+1
			grosor=5
			blue=255
			green=0
			red=0
		else:
			grosor=3
			blue=0
			green=255
			red=0
		
		texto = str(cuenta)
		#texto1 = str(b)
		#texto2 = str(mh)
		#cv2.putText(frame, texto1, (0,mh+30), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)
		#cv2.putText(frame, texto2, (0,mh), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)
		cv2.putText(frame, texto, (0,mh), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)
	
	#lines = cv2.HoughLines(edges,1,np.pi/180,200)
	lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
	for x1,y1,x2,y2 in lines[0]:
		frame=cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5,8)

	#frame2 = cv2.line(frame, (0,mh) , (2*mw,mh), (blue,green,red), grosor, 8)

	#cv2.imshow('Video',frame3)
	cv2.imshow('Video',frame)
	cv2.imshow('Esquinas',edges)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()
