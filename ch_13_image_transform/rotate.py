import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./cmes.png')
img = cv2.resize(img, None, None, 0.5, 0.5)
h, w, _ = img.shape

d30 = 30 * np.pi / 180
d60 = 60 * np.pi / 180

m30 = np.float32([[np.cos(d30), -1*np.sin(d30), w//3],
                  [np.sin(d30), np.cos(d30), -1*w//4]])
m60 = np.float32([[np.cos(d60), -1*np.sin(d60), w//1.5],
                  [np.sin(d60), np.cos(d60), -1*w//4]])

r30 = cv2.warpAffine(img, m30, (h, w))
r60 = cv2.warpAffine(img, m60, (w, h))

# cv2.getRotationMatrix2D
m30_2 = cv2.getRotationMatrix2D((w//2, h//2), 30, 1)
m60_2 = cv2.getRotationMatrix2D((w//2, h//2), 60, 1)

img30 = cv2.warpAffine(img, m30_2, (w, h))
img60 = cv2.warpAffine(img, m60_2, (w, h))

cv2.imshow('Original', img)
cv2.imshow('30', r30)
cv2.imshow('60', r60)
cv2.imshow('30 OpenCV', img30)
cv2.imshow('60 OpenCV', img60)
cv2.waitKey(0)
cv2.destroyAllWindows()