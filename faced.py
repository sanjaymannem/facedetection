import numpy
import cv2
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier('haarcascade_eye.xml')
cap= cv2.VideoCapture(0)
while True:
	ret,img=cap.read()
	gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	faces=face.detectMultiScale(gray)
	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		gray2=gray[y:y+h,x:x+w]
		color=img[y:y+h,x:x+w]
		eyes=eye.detectMultiScale(gray2)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
	cv2.imshow('img',img)
	k=cv2.waitKey(30)&0xff
	if k==27:
		break
cap.relese()
cv2.destroiAllwindows