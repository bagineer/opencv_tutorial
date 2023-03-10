import cv2
import numpy as np
import os.path as osp

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'leaflet.jpg'
img_file = osp.join(file_path, file_name)
img = cv2.imread(img_file)
img2 = img.copy()
draw = img.copy()

pts1 = np.float32([[300, 300], [100, 600], [500, 500]])
pts2 = np.float32([[100, 200], [300, 500], [600, 400]])

x1, y1, w1, h1 = cv2.boundingRect(pts1)
x2, y2, w2, h2 = cv2.boundingRect(pts2)

roi1 = img[y1:y1+h1, x1:x1+w1]
roi2 = img[y2:y2+h2, x2:x2+w2]

offset1 = np.zeros((3, 2), dtype=np.float32)
offset2 = np.zeros((3, 2), dtype=np.float32)

for i in range(3):
    offset1[i][0], offset1[i][1] = pts1[i][0] - x1, pts1[i][1] - y1
    offset2[i][0], offset2[i][1] = pts2[i][0] - x2, pts2[i][1] - y2

m = cv2.getAffineTransform(offset1, offset2)
warped = cv2.warpAffine(roi1, m, (w2, h2), None,
                        cv2.INTER_LINEAR, cv2.BORDER_REFLECT101)

mask = np.zeros((h2, w2), dtype=np.uint8)
cv2.fillConvexPoly(mask, np.int32(offset2), (255))

warped_masked = cv2.bitwise_and(warped, warped, mask=mask)
roi2_masked = cv2.bitwise_and(roi2, roi2, mask=cv2.bitwise_not(mask))
roi2_masked += warped_masked
img2[y2:y2+h2, x2:x2+w2] = roi2_masked

cv2.rectangle(draw, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
cv2.polylines(draw, [pts1.astype(np.int32)], True, (0, 255, 0), 1)
cv2.rectangle(img2, (x2, y2), (x2+w2, y2+h2), (0, 0, 255), 2)
cv2.polylines(img2, [pts2.astype(np.int32)], True, (0, 255, 0), 1)

cv2.imshow('Original', draw)
cv2.imshow('Triangle Affine', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()