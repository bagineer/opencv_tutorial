import cv2
import numpy as np

img = cv2.imread('./silhouette.jpg', cv2.IMREAD_GRAYSCALE)
_, img_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

dist = cv2.distanceTransform(img_bin, cv2.DIST_L2, 5)
dist = (dist / (dist.max() - dist.min()) * 255).astype(np.uint8)

skeleton = cv2.adaptiveThreshold(dist, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 7, -3)

merged = np.hstack((img, dist, skeleton))

compare = cv2.cvtColor(dist, cv2.COLOR_GRAY2BGR)
compare[skeleton>0] = [0, 255, 0]

cv2.imshow('Distance Transform', merged)
cv2.imshow('Compare', compare)
cv2.waitKey()
cv2.destroyAllWindows()