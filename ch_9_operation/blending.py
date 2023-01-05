import cv2
import numpy as np
from matplotlib import pyplot as plt

# simple blending
img1 = cv2.imread('./lion.jpg')
img2 = cv2.imread('./tiger.jpg')
h1, w1, _ = img1.shape
h2, w2, _ = img2.shape
mh, mw = min(h1, h2), min(w1, w2)
dh, dw = h1 - mh, w2 - mw

img1 = img1[dh//2:dh//2+mh, dw//2:dw//2+mw, :]  # crop bigger image by small image sizes

img3 = img1 + img2          # adding by numpy operation
img4 = cv2.add(img1, img2)  # adding by cv2

# alpha blending
alpha = 0.3
img5 = img1 * alpha + img2 * (1 - alpha)
img5 = img5.astype(np.uint8)
img6 = cv2.addWeighted(img1, alpha, img2, 1-alpha, 0)

imgs = {'img1': img1, 'img2': img2, 'img1 + 1mg2 (numpy)': img3, 'cv2.add(img1, img2)': img4,
        'img1 + img2 (numpy alpha)': img5, 'cv2.addWeighted(img1, img2), alpha=0.5': img6}

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(3, 2, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)
    plt.xticks([])
    plt.yticks([])
plt.show()