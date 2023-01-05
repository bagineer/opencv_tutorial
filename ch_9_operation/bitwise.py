import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = np.zeros((200, 200), dtype=np.uint8)
img1[:, :100] = 1 # 255
img2 = np.zeros((200, 200), dtype=np.uint8)
img2[100:, :] = 1 # 255

bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img1, img2)
bit_xor = cv2.bitwise_xor(img1, img2)
bit_not = cv2.bitwise_not(img1)

imgs = {'img1': img1, 'img2': img2, 'and': bit_and,
        'or': bit_or, 'xor': bit_xor, 'not img1': bit_not}

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(3, 2, i+1)
    plt.imshow(v, 'gray')
    plt.title(k)
    plt.xticks([])
    plt.yticks([])
plt.show()