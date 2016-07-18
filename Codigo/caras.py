import numpy as np
import cv2
 
image = cv2.imread('People.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread('rostro.jpg',0)
w,h = template.shape[::-1]

res = cv2.matchTemplate(image_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.75
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',image)
cv2.waitKey(0)
