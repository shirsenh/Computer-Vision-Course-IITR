from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt

lena = misc.imread('images.jpg')

lena = lena[:,:,0]

from skimage.feature import canny


edge1 = canny(lena, sigma=3, low_threshold=10, high_threshold=80)
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3), sharex=True, sharey=True)


ax1.imshow(lena, cmap=plt.cm.gray)
ax1.axis('off')

ax2.imshow(edge1, cmap=plt.cm.gray)
ax2.axis('off')

fig.tight_layout()

plt.show()

import numpy as np
from skimage.restoration import (denoise_tv_chambolle, estimate_sigma)
from skimage import data, img_as_float, color
from skimage.util import random_noise

original = img_as_float(lena)
sigma = 0.155

noisy = random_noise(original, var=sigma**2)

fig, (ax4, ax5, ax6) = plt.subplots(nrows=1, ncols=3, figsize=(8, 5), sharex=True, sharey=True)

ax4.imshow(original, cmap=plt.cm.gray)
ax4.axis('off')

ax5.imshow(noisy, cmap=plt.cm.gray)
ax5.axis('off')

denoise = denoise_tv_chambolle(noisy, weight=0.25, multichannel=True)
ax6.imshow(denoise, cmap=plt.cm.gray)
ax6.axis('off')

fig.tight_layout()
plt.show()
