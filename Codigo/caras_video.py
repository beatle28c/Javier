import numpy as np
import cv2
 
camera = cv2.VideoCapture(0)	#define la captura de video, 0 es default
cara = cv2.imread('r2d2.jpg',0) 
w,h = cara.shape[::-1]

while True:
	ret, frame = camera.read()	#lee de la camara.
	if ret == True:	
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)	#convierte a escala de grises
	
	
	res = cv2.matchTemplate(gray,cara,cv2.TM_CCOEFF_NORMED)
	threshold = 0.8
	loc = np.where(res >= threshold)
	
	for pt in zip(*loc[::-1]):
		cv2.rectangle(frame, pt, (pt[0]+w,pt[1]+h),(0,255,255),2)
	
	cv2.imshow('Frame',frame)
	if cv2.waitKey(1)==ord('q'):
		break
		
camera.release()
cv2.destroyAllWindows()
