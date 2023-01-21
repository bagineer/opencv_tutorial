import cv2
import numpy as np
import os.path as osp

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'cmes.png'
img_file = osp.join(file_path, file_name)
img = cv2.imread(img_file)
img = cv2.resize(img, (256, 256))
h, w, _ = img.shape
dx, dy = 100, 100

M = np.float32([[1, 0, dx],
                   [0, 1, dy]])
dst = cv2.warpAffine(img, M, (w+dx, h+dy))
dst2 = cv2.warpAffine(img, M, (w+dx, h+dy), None,
                      cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, (0, 255, 0))
dst3 = cv2.warpAffine(img, M, (w+dx, h+dy), None,
                      cv2.INTER_LINEAR, cv2.BORDER_REFLECT)

cv2.imshow('Original', img)
cv2.imshow('Defualt', dst)
cv2.imshow('Constant', dst2)
cv2.imshow('Reflect', dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()