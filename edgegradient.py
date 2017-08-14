import cv2
import numpy as np 

cap = cv2.imread('image.png')
cv2.imshow('cap',cap)
sobelx = cv2.Sobel(cap,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(cap,cv2.CV_64F,0,1,ksize=5)
edges = cv2.Canny(cap,200,200)

laplacian = cv2.Laplacian(cap, cv2.CV_64F)
cv2.imshow('laplacian', laplacian)
cv2.imshow('sobelx', sobelx)
cv2.imshow('sobely', sobely)
cv2.imshow('edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()