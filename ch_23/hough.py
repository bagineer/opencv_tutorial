import cv2
import os.path as osp
import numpy as np

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'sample.jpg'
img = cv2.imread(osp.join(file_path, file_name))
# img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
copied1 = img.copy()
copied2 = img.copy()
copied3 = img.copy()
h, w, _ = img.shape

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img_gray, 100, 200)

# Hough Line Transform
lines = cv2.HoughLines(edges, 1, np.pi/180, 70)
for line in lines:
    r, theta = line[0]
    tx, ty = np.cos(theta), np.sin(theta)
    x0, y0 = tx*r, ty*r
    cv2.circle(copied1, (abs(x0), abs(y0)), 3, (0, 0, 255), -1)

    x1, y1 = int(x0 - w*ty), int(y0 + h*tx)
    x2, y2 = int(x0 + w*ty), int(y0 - h*tx)

    cv2.line(copied1, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Probabilistic Hough Line Transform
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 5, None, 20, 2)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(copied2, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Hough Circle Transform
blurred = cv2.GaussianBlur(img_gray, (3, 3), 0)

circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 2, 30, None, 200)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for x, y, r in circles[0, :]:
        cv2.circle(copied3, (x, y), r, (255, 0, 0), 2)
        cv2.circle(copied3, (x, y), 4, (0, 0, 255), -1)

merged1 = np.hstack((img, copied1))
merged2 = np.hstack((copied2, copied3))
merged = np.vstack((merged1, merged2))
cv2.imshow('Hough', merged)
cv2.imshow('Edge', edges)
cv2.waitKey()
cv2.destroyAllWindows()