import cv2
import numpy as np
import os.path as osp
from matplotlib import pyplot as plt

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'tiger.jpg'
img_file = osp.join(file_path, file_name)
img = cv2.imread(img_file)

mask = np.zeros_like(img)
masking_value = 127
cv2.rectangle(mask, (200, 100), (600, 400), (0, 0, 255), -1)

masked = cv2.bitwise_and(img, mask)

imgs = {'original': img, 'mask': mask, 'masked': masked}

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)
    plt.xticks([])
    plt.yticks([])
plt.show()