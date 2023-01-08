import cv2
import numpy as np

img = cv2.imread('./sample.jpg')
h, w, _ = img.shape

pts1 = np.float32([[0, 0], [0, h], [w, 0], [w, h]])
pts2 = np.float32([[150, 100], [20, h-50], [w-150, 100], [w-20, h-50]])

for i, (x, y) in enumerate(pts1):
    color = [0, 0, 0]
    color[i%3] = 255
    if i > 2:
        color[1] = 255
    cv2.circle(img, (x, y), 20, color, -1)

m = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, m, (w, h))

cv2.imshow('Original', img)
cv2.imshow('Perspective', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()