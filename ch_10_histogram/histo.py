import cv2
import numpy as np
from matplotlib import pyplot as plt


## Gray Scale
img_gray = cv2.imread('./Lenna.png', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])

plt.figure('Gray Scale')
plt.subplot(2, 1, 1)
plt.imshow(img_gray, 'gray')
plt.title('image')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 1, 2)
plt.plot(hist)
# plt.show()


## Color
img = cv2.imread('./Lenna.png')
plt.figure('Color')
plt.subplot(1, 2, 1)
plt.imshow(img[:, :, ::-1])
plt.title('image')
plt.xticks([])
plt.yticks([])

colors = ['b', 'g', 'r']
for i, color in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.subplot(1, 2, 2)
    plt.plot(hist, color=color)

## Normalize
# dynamic range 조정
img_f = img_gray.astype(np.float32)
img_f = (img_f - img_f.min()) * 100 / (img_f.max() - img_f.min()) + 100
img_dr = img_f.astype(np.uint8)

img_f = img_dr.astype(np.float32)
img_norm = ((img_f - img_f.min()) * 255 / (img_f.max() - img_f.min()))
img_norm = img_norm.astype(np.uint8)

img_norm2 = cv2.normalize(img_f, None, 0, 255, cv2.NORM_MINMAX)

hist = cv2.calcHist([img_dr], [0], None, [256], [0, 256])
hist_norm = cv2.calcHist([img_norm], [0], None, [256], [0, 256])
hist_norm2 = cv2.calcHist([img_norm2], [0], None, [256], [0, 256])

imgs = {'original': img_dr, 'img_norm': img_norm, 'img_norm2': img_norm2}
hists = {'original': hist, 'hist_norm': hist_norm, 'hist_norm2': hist_norm2}

plt.figure('Normalize')
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 3, i+1)
    plt.imshow(v, 'gray', vmin=0, vmax=255)
    plt.title(k)
    plt.xticks([])
    plt.yticks([])

for i, (k, v) in enumerate(hists.items()):
    plt.subplot(2, 3, i+4)
    plt.plot(v)
    plt.title(k)

## Equalize
h, w = img_dr.shape

hist = cv2.calcHist([img_dr], [0], None, [256], [0, 256])
cdf = hist.cumsum()
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) / (h * w) * 255
cdf = np.ma.filled(cdf_m, 0).astype(np.uint8)
img_eq1 = cdf[img_dr]

img_eq2 = cv2.equalizeHist(img_dr)

hist_eq1 = cv2.calcHist([img_eq1], [0], None, [256], [0, 256])
hist_eq2 = cv2.calcHist([img_eq2], [0], None, [256], [0, 256])

imgs = {'original': img_dr, 'eq1': img_eq1, 'eq2': img_eq2}
hists = {'original': hist, 'manual': hist_eq1, 'cv2.equlizeHist': hist_eq2}

plt.figure('Equalize')
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 3, i+1)
    plt.imshow(v, 'gray', vmin=0, vmax=255)
    plt.title(k)
    plt.xticks([])
    plt.yticks([])

for i, (k, v) in enumerate(hists.items()):
    plt.subplot(2, 3, i+4)
    plt.plot(v)
    plt.title(k)

plt.show()

