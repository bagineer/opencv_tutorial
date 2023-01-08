import cv2
import numpy as np

ALPHA_WIDTH_RATE = 15

tiger = cv2.imread('./tiger.jpg')
lion = cv2.imread('./lion.jpg')
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