import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

img = cv2.imread('./sample.jpg')
h, w, _ = img.shape

# Flip with matrix
st = time.time()
mflip = np.float32([[-1, 0, w-1], [0, -1, h-1]])
fliped1 = cv2.warpAffine(img, mflip, (w, h))
print(f'matrix : {time.time() - st}')

# Flip with remap
st = time.time()
mapy, mapx = np.indices((h, w), dtype=np.float32)
mapx = w - mapx - 1
mapy = h - mapy - 1

fliped2 = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
print(f'remap : {time.time() - st}')

# Remap sin & cos
WAVE_LENGTH = 10
AMP = 5

mapy, mapx = np.indices((h, w), dtype=np.float32)
sinx = mapx + AMP * np.sin(mapy/WAVE_LENGTH)
siny = mapy + AMP * np.sin(mapx/WAVE_LENGTH)
cosx = mapx + AMP * np.cos(mapy/WAVE_LENGTH)
cosy = mapy + AMP * np.cos(mapx/WAVE_LENGTH)

img_sinx = cv2.remap(img, sinx, mapy, cv2.INTER_LINEAR)
img_siny = cv2.remap(img, mapx, siny, cv2.INTER_LINEAR)
img_cosx = cv2.remap(img, cosx, mapy, cv2.INTER_LINEAR)
img_cosy = cv2.remap(img, mapx, cosy, cv2.INTER_LINEAR)
img_both = cv2.remap(img, sinx, cosy, cv2.INTER_LINEAR)

cv2.imshow('Original', img)
cv2.imshow('Fliped 1', fliped1)
cv2.imshow('Fliped 2', fliped2)

imgs = {'Original': img, 'sinx': img_sinx, 'cosy': img_cosy,
        'sinx cosy': img_both, 'cosx': img_cosx, 'siny': img_siny}
plt.figure('Remap sin cos')
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 3, i+1)
    plt.title(k)
    plt.axis('off')
    plt.imshow(v[:, :, ::-1])

# Remap sin with other wave length & amp
wave_lengths = [10, 20]
amps = [5, 10]

imgs = dict()
i = 0
for wl in wave_lengths:
    for amp in amps:
        i += 1
        siny = mapy + amp * np.sin(mapx/wl)
        img_sin = cv2.remap(img, mapx, siny, cv2.INTER_LINEAR)
        imgs[f'siny{i}_wavelength{wl}_amp{amp}'] = img_sin

plt.figure('Wave length and amplitude')
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 2, i+1)
    plt.title(k)
    plt.axis('off')
    plt.imshow(v[:, :, ::-1])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()