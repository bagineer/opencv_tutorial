import cv2
import numpy as np

# Harris Corner Detection
img = cv2.imread('./sample.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corner = cv2.cornerHarris(gray, 2, 7, 0.2)
coords = np.where(corner > 0.1 * corner.max())
coords = np.stack((coords[1], coords[0]), axis = -1)

for i, (x, y) in enumerate(coords):
    cv2.circle(img, (x, y), 5, (min(i, 255), 255 - min(i, 255), 0), 1, cv2.LINE_AA)

corner_norm = cv2.normalize(corner, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
corner_norm = cv2.cvtColor(corner_norm, cv2.COLOR_GRAY2BGR)

merged = np.hstack((corner_norm, img))
cv2.imshow('Harris', merged)





cv2.waitKey()
cv2.destroyAllWindows()