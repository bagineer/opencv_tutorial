import cv2
import numpy as np

img = cv2.imread('./lines2.png')
img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
copied = img.copy()
h, w, _ = img.shape

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img_gray, 50, 230)
lines = cv2.HoughLines(edges, 1, np.pi/180, 150)

for line in lines:
    r, theta = line[0]
    tx, ty = np.cos(theta), np.sin(theta)
    x0, y0 = tx*r, ty*r
    cv2.circle(copied, (abs(x0), abs(y0)), 3, (0, 0, 255), -1)

    x1, y1 = int(x0 - w*ty), int(y0 + h*tx)
    x2, y2 = int(x0 + w*ty), int(y0 - h*tx)

    cv2.line(copied, (x1, y1), (x2, y2), (0, 255, 0), 1)

merged = np.hstack((img, copied))
cv2.imshow('Hough', merged)
cv2.imshow('Edge', edges)
cv2.waitKey()
cv2.destroyAllWindows()