import cv2 
import numpy as np 

cap = cv2.imread('watch.jpg')
while True:
	hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
	lower_blue = np.array([50,100,50])
	upper_blue = np.array([255,255,255])

	mask = cv2.inRange(hsv,lower_blue,upper_blue)
	res = cv2.bitwise_and(cap,cap, mask = mask)
	kernel = np.ones((15,15),np.float32)/225
	smoothed = cv2.filter2D(res,-1,kernel)
	blur = cv2.GaussianBlur(res, (15,15),0)
	median = cv2.medianBlur(res,15)
	bilateral = cv2.bilateralFilter(res, 15, 200,200)
	
	cv2.imshow('smoothed',smoothed)
	cv2.imshow('blur', blur)
	cv2.imshow('median', median)
	cv2.imshow('bilateral',bilateral)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break


cv2.waitKey(0)
cv2.destroyAllWindows()