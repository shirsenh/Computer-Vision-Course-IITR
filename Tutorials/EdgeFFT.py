import cv2
import numpy as np
from matplotlib import pyplot as plt

# loading image
#img0 = cv2.imread('SanFrancisco.jpg',)
img0 = cv2.imread('lena.png',)

# converting to gray scale
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(gray,(3,3),0)

# convolute with proper kernels
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=1)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=1)  # y

# in freq domain
img = cv2.imread('lena.png',0)

rows, cols = img.shape
crow,ccol  = rows//2 , cols//2

dft 		= cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift 	=np.fft.fftshift(dft)
# create a mask first, center square is 1, remaining all zeros
mask 		= np.zeros((rows,cols,2),np.uint8)
boxSizeRow	= 20
boxSizeCol	= 20
mask[crow-boxSizeRow:crow+boxSizeRow , ccol-boxSizeCol:ccol+boxSizeCol] = 1
mask = 1- mask

# apply mask and inverse DFT
fshift 	 	= dft_shift*mask
f_ishift 	= np.fft.ifftshift(fshift)
img_back 	= cv2.idft(f_ishift)
img_back 	= cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(1,2,1),plt.imshow(img , cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(3,2,2),plt.imshow(laplacian)
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
# plt.subplot(3,2,3),plt.imshow(sobelx)
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(3,2,4),plt.imshow(sobely)
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(img_back , cmap = 'gray')
plt.title('FFT'), plt.xticks([]), plt.yticks([])


plt.show()
# via inbuilt edge detector
# cv2.imshow('sobelx',sobelx)
# cv2.imshow('sobely',sobely)
# cv2.imshow('laplacian',laplacian)
plt.show()
cv2.waitKey(0)
# plt.show()