import cv2
import sys

#cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
javiercascade = cv2.CascadeClassifier('cascade.xml')
#haarcascade_eye
video_capture = cv2.VideoCapture(0)
font=cv2.FONT_HERSHEY_SIMPLEX
n = 0
while True:

    ret, frame = video_capture.read()

    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	faces = faceCascade.detectMultiScale(
		frame,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE
		)


	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		#cv2.putText(frame,number,(x+w, y+h), font, 1, (200,255,155), 1, cv2.LINE_AA)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		#javier_cara = javiercascade.detectMultiScale(roi_gray)
		#for (jx, jy, jw, jh) in javier_cara:
		#	cv2.rectangle(roi_color, (jx, jy), (jx+jw, jy+jh), (255, 255, 0), 2)


        # Display the resulting frame
	cv2.imshow('Video', frame)
	#cv2.imshow('Gray', gray)

	if cv2.waitKey(1)==ord('q'):
		break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
