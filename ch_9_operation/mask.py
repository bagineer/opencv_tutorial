import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./tiger.jpg')

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