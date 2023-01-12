import cv2
import numpy as np

# Harris Corner Detection
img = cv2.imread('./sample.jpg')
img_draw = img.copy()
gray = cv2.cvtColor(img_draw, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', img)

corner = cv2.cornerHarris(gray, 2, 7, 0.2)
coords = np.where(corner > 0.1 * corner.max())
coords = np.stack((coords[1], coords[0]), axis = -1)

for i, (x, y) in enumerate(coords):
    cv2.circle(img_draw, (x, y), 5, (min(i, 255), 255 - min(i, 255), 0), 1, cv2.LINE_AA)

corner_norm = cv2.normalize(corner, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
corner_norm = cv2.cvtColor(corner_norm, cv2.COLOR_GRAY2BGR)

cv2.imshow('Harris', img_draw)

# Shi-Tomasi Detection
img_draw = img.copy()
corners = cv2.goodFeaturesToTrack(gray, 30, 0.01, 10)
corners = np.int32(corners)

for i, corner in enumerate(corners):
    x, y = corner[0]
    cv2.circle(img_draw, (x, y), 3, (min(i, 255), 0, 255 - min(i, 255)), 1, cv2.LINE_AA)

cv2.imshow('GFTT Shi - Tomasi', img_draw)



cv2.waitKey()
cv2.destroyAllWindows()