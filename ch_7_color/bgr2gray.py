import cv2 as cv
import numpy as np
import os.path as osp

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'sample.png'
img_file = osp.join(file_path, file_name)
image = cv.imread(img_file)
print(image.shape)

uint_image = image.astype(np.uint16)
b, g, r = cv.split(uint_image)
gray_mean = ((b + g + r) / 3).astype(np.uint8)
gray_cvt = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
color_cvt = cv.cvtColor(gray_cvt, cv.COLOR_GRAY2BGR)
print(gray_mean.shape, gray_cvt.shape, color_cvt.shape)

cv.imshow('Color', image)
cv.imshow('Gray Mean', gray_mean)
cv.imshow('Gray Convert', gray_cvt)
cv.imshow('Color Convert', color_cvt)

cv.waitKey(0)
cv.destroyAllWindows()