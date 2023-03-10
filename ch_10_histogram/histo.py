import cv2
import numpy as np
import os.path as osp
from matplotlib import pyplot as plt


## Gray Scale

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'Lenna.png'
img_gray = cv2.imread(osp.join(file_path, file_name), cv2.IMREAD_GRAYSCALE)

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
img = cv2.imread(osp.join(file_path, file_name))
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


## Equalize Color
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])
img_eq = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

imgs = {'original': img, 'equalized': img_eq}

plt.figure('Equlize Color')
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(1, 2, i+1)
    plt.title(k)
    plt.imshow(v[:, :, ::-1])
    plt.xticks([])
    plt.yticks([])

## CLAHE
img_f2 = img.astype(np.float32)
img_bright = (img_f2 - img_f2.min()) / (img_f2.max() - img_f2.min()) * 55 + 200
img_bright = img_bright.astype(np.uint8)

img_hsv = cv2.cvtColor(img_bright, cv2.COLOR_BGR2HSV)

img_eq = img_hsv.copy()
img_eq[:, :, 2] = cv2.equalizeHist(img_eq[:, :, 2])
img_eq = cv2.cvtColor(img_eq, cv2.COLOR_HSV2BGR)

img_clahe1 = img_hsv.copy()
clahe = cv2.createCLAHE(10, (10, 10))
img_clahe1[:, :, 2] = clahe.apply(img_clahe1[:, :, 2])
img_clahe1 = cv2.cvtColor(img_clahe1, cv2.COLOR_HSV2BGR)

img_clahe2 = img_hsv.copy()
clahe = cv2.createCLAHE(5, (10, 10))
img_clahe2[:, :, 2] = clahe.apply(img_clahe2[:, :, 2])
img_clahe2 = cv2.cvtColor(img_clahe2, cv2.COLOR_HSV2BGR)

imgs = {'original': img_bright, 'equalization': img_eq,
        'CLAHE 10': img_clahe1, 'CLAHE 5': img_clahe2}

plt.figure('CLAHE')
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 2, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)
    plt.xticks([])
    plt.yticks([])

plt.show()

