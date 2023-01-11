import cv2
import numpy as np

target = cv2.imread('./4star.jpg')
shapes = cv2.imread('./shapestomatch.jpg')
h = shapes.shape[0]
coppied = cv2.resize(target, (h, h), None)
shapes = np.hstack((coppied, shapes))

t_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
s_gray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)

_, th_target = cv2.threshold(t_gray, 127, 255, cv2.THRESH_BINARY_INV)
_, th_shapes = cv2.threshold(s_gray, 127, 255, cv2.THRESH_BINARY_INV)

_, t_contour, _ = cv2.findContours(th_target, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
_, s_contour, _ = cv2.findContours(th_shapes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

matches = []
for contour in s_contour:
    matched = cv2.matchShapes(t_contour[0], contour, cv2.CONTOURS_MATCH_I2, 0.0)
    matches.append((matched, contour))
    cv2.putText(shapes, f'{matched:.2f}', tuple(contour[0][0]),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

matches.sort(key = lambda x: x[0])

cv2.drawContours(shapes, [matches[0][1]], -1, (0, 255, 0), 3)
cv2.drawContours(shapes, [matches[1][1]], -1, (255, 0, 0), 3)
cv2.imshow('target', target)
cv2.imshow('shapes', shapes)
cv2.waitKey()
cv2.destroyAllWindows()
