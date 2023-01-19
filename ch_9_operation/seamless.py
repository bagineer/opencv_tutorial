import cv2
import numpy as np
import os.path as osp
from matplotlib import pyplot as plt

file_path = osp.dirname(osp.abspath(__file__))
img_src = osp.join(file_path, 'chromakey.jpg')
img_dst = osp.join(file_path, 'antarctica.jpg')
src = cv2.imread(img_src)
dst = cv2.imread(img_dst)

mask = np.full_like(src, 255)

h, w, _ = dst.shape
center_point = (w//2, h//2)
print(h, w, center_point, dst.shape)

normal = cv2.seamlessClone(src, dst, mask, center_point, cv2.NORMAL_CLONE)
mixed = cv2.seamlessClone(src, dst, mask, center_point, cv2.MIXED_CLONE)

imgs = {'src': src, 'dst': dst, 'normal': normal, 'mixed':mixed}

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 2, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)
    plt.xticks([])
    plt.yticks([])
plt.show()