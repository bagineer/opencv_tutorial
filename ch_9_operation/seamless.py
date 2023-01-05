import cv2
import numpy as np
from matplotlib import pyplot as plt

src = cv2.imread('./chromakey.jpg')
dts = cv2.imread('./antarctica.jpg')

mask = np.full_like(src, 255)

h, w, _ = dts.shape
center_point = (w//2, h//2)
print(h, w, center_point, dts.shape)

normal = cv2.seamlessClone(src, dts, mask, center_point, cv2.NORMAL_CLONE)
mixed = cv2.seamlessClone(src, dts, mask, center_point, cv2.MIXED_CLONE)

imgs = {'src': src, 'dts': dts, 'normal': normal, 'mixed':mixed}

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 2, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)
    plt.xticks([])
    plt.yticks([])
plt.show()