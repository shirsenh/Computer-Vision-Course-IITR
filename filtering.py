import cv2 
import numpy as np 

cap = cv2.imread('watch.jpg')
while True:
	hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
	lower_blue = np.array([50,150,50])
	upper_blue = np.array([255,255,255])

	mask = cv2.inRange(hsv,lower_blue,upper_blue)
	res = cv2.bitwise_and(cap,cap, mask = mask)
	cv2.imshow('cap',cap)
	cv2.imshow('res', res)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break


cv2.waitKey(0)
cv2.destroyAllWindows()