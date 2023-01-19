import cv2 as cv
import os.path as osp

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'sample.png'
img_file = osp.join(file_path, file_name)
image = cv.imread(img_file)
print(image.shape)
bgr = cv.imread(img_file, cv.IMREAD_COLOR)
bgra = cv.imread(img_file, cv.IMREAD_UNCHANGED)

cv.imshow('Color', image)
cv.imshow('BGR', bgr)
cv.imshow('B', bgra[:, :, 0])
cv.imshow('G', bgra[:, :, 1])
cv.imshow('R', bgra[:, :, 2])
cv.imshow('A', bgra[:, :, 3])
cv.waitKey(0)
cv.destroyAllWindows()