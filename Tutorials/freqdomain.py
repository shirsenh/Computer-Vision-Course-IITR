import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('tom.jpg',0)

dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

rows, cols = img.shape
crow,ccol = rows/2 , cols/2

# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

# create a mask first, center square is 0, remaining all ones
mask2 = np.ones((rows, cols,2), np.uint8)
mask2[crow-30:crow+30, ccol-30:ccol+30] = 0

# apply mask and inverse DFT
fshift = dft_shift*mask
fshift2 = dft_shift*mask2

f_ishift = np.fft.ifftshift(fshift)
f_ishift2 = np.fft.ifftshift(fshift2)

img_back = cv2.idft(f_ishift)
img_back2 = cv2.idft(f_ishift2)

img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
img_back2 = cv2.magnitude(img_back2[:,:,0],img_back2[:,:,1])

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Low Pass Filter\nSmoothing'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back2, cmap = 'gray')
plt.title('High Pass Filter\nEdge Detection'), plt.xticks([]), plt.yticks([])
plt.show()