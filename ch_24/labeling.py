import cv2
import os.path as osp
import numpy as np

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'silhouette.jpg'
img_file = osp.join(file_path, file_name)
img = cv2.imread(img_file)
labeled = np.zeros_like(img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_bin = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

cnt, labels = cv2.connectedComponents(img_bin)
for i in range(cnt):
    labeled[labels==i] = [int(j) for j in np.random.randint(0, 255, 3)]

merged = np.hstack((img, labeled))
cv2.imshow('Labeling', merged)
cv2.waitKey()
cv2.destroyAllWindows()