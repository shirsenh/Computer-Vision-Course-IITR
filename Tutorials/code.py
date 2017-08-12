import cv2
import numpy as np
import time
from matplotlib import pyplot as plt


def vertical_diff(img):
	img2 = np.copy(img)
	for i in range(1, img2.shape[0]-1):
		for j in range(1, img2.shape[1]-1):
			img2[i][j] = img2[i][j] - (img2[i][j-1]+img2[i][j+1])/2
	return img2

def horizontal_diff(img):
	img2 = np.copy(img)
	for i in range(1, img2.shape[0]-1):
		for j in range(1, img2.shape[1]-1):
			img2[i][j] = img2[i][j] - (img2[i-1][j]+img2[i+1][j])/2
	return img2

def blur(img):
	img2 = np.copy(img)
	for i in range(1, img2.shape[0]-1):
		for j in range(1, img2.shape[1]-1):
			img2[i][j] = (img2[i-1][j]+img2[i][j]+img2[i+1][j]+img2[i-1][j-1]+img2[i][j-1]+img2[i+1][j-1]+img2[i+1][j+1]+img2[i][j+1]+img2[i-1][j+1])/9
	return img2

def median_filter_noise_removal(img):
	img2 = np.copy(img)
	for i in range(1, img2.shape[0]-1):
		for j in range(1, img2.shape[1]-1):
			arr = np.array([img2[i-1][j], img2[i][j], img2[i+1][j], img2[i-1][j-1], img2[i][j-1], img2[i+1][j-1], img2[i+1][j+1], img2[i][j+1], img2[i-1][j+1]])
			img2[i][j] = np.median(arr)
	return img2


def laplacian(img):
	img2 = np.copy(img)
	for i in range(1, img2.shape[0]-1):
		for j in range(1, img2.shape[1]-1):
			img2[i][j] = (img2[i-1][j]-8*img2[i][j]+img2[i+1][j]+img2[i-1][j-1]+img2[i][j-1]+img2[i+1][j-1]+img2[i+1][j+1]+img2[i][j+1]+img2[i-1][j+1])/9
	return img2

imname = "penguin.jpg"
img = cv2.imread(imname,0)


##############################    EDGE DETECTION   ################################

cv2.imshow("Orginal",img)
img2 = vertical_diff(img)
cv2.imshow("Vertical Diff",img2)
img3 = horizontal_diff(img)
cv2.imshow("Horizontal Diff",img3)
img4 = blur(img)
cv2.imshow("BLUR",img4)
img_avg = (img3+img4)/2
cv2.imshow("Average Difference",img_avg)
img7 = laplacian(img)
cv2.imshow("Laplacian",img7)

cv2.waitKey(0)
time.sleep(5)
cv2.destroyAllWindows()

##############################    NIOSE REMOVAL   ################################

imname = "noise_lena.png"
img = cv2.imread(imname,0)
img_nr = median_filter_noise_removal(img)
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_nr, cmap = 'gray')
plt.title('After Noise Removal'), plt.xticks([]), plt.yticks([])
plt.show()
