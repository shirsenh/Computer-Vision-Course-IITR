import cv2 
import numpy as np 

cap = cv2.imread('watch.jpg')
while True:
	hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
	lower_blue = np.array([50,100,50])
	upper_blue = np.array([255,255,255])

	mask = cv2.inRange(hsv,lower_blue,upper_blue)
	res = cv2.bitwise_and(cap,cap, mask = mask)

	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(mask,kernel,iterations = 1)
	dilation = cv2.dilate(mask,kernel, iterations = 1)
	opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
	closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

	cv2.imshow('res',res)
	cv2.imshow('dilation', dilation)
	cv2.imshow('erosion', erosion)
	cv2.imshow('closing',closing)
	cv2.imshow('opening', opening)
	cv2.imshow('Tophat',tophat)
	cv2.imshow('Blackhat',blackhat)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break


cv2.waitKey(0)
cv2.destroyAllWindows()