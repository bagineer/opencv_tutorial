import cv2
import numpy as np
import os.path as osp

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'sample.jpg'
img_file = osp.join(file_path, file_name)
img = cv2.imread(img_file)
h, w, _ = img.shape
print(h, w)

pts1 = np.float32([[100, 100], [400, 100], [400, 300]])
pts2 = np.float32([[50, 70], [300, 70], [400, 130]])

for i, (x, y) in enumerate(pts1):
    color = [0, 0, 0]
    color[i] = 255
    cv2.circle(img, (x, y), 5, color, -1)

m = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, m, (w, h))

cv2.imshow('Original', img)
cv2.imshow('Affine', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()