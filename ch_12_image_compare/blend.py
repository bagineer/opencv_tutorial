import cv2
import numpy as np
import os.path as osp

ALPHA_WIDTH_RATE = 15

file_path = osp.dirname(osp.abspath(__file__))
img_tiger = osp.join(file_path, 'tiger.jpg')
img_lion = osp.join(file_path, 'lion.jpg')
tiger = cv2.imread(img_tiger)
lion = cv2.imread(img_lion)
blended = np.zeros_like(tiger)

h, w, _ = tiger.shape
m = w // 2
alpha_w = w * ALPHA_WIDTH_RATE // 100
s = m - alpha_w // 2
step = 100 / alpha_w

blended[:, :m, :] = tiger[:, :m, :].copy()
blended[:, m:, :] = lion[:, m:, :].copy()
cv2.imshow('Half', blended)

for i in range(alpha_w+1):
    a = 1 - step*i / 100
    b = 1 - a
    blended[:, s+i] = tiger[:, s+i]*a + lion[:, s+i]*b
    print(a, b)
cv2.imshow('Blended', blended)

cv2.waitKey()
cv2.destroyWindow()