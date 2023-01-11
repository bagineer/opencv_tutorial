import cv2
import numpy as np

img = cv2.imread('./sample.png')
h, w, _ = img.shape
img = cv2.resize(img, (w//2, h//2), interpolation=cv2.INTER_LINEAR)
coppied = img.copy()

img_gray = img[:, :, 0]
ret, img_binary = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)

_, contour, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_NONE)
_, contour2, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contour, -1, (255, 0, 0), 8)
cv2.drawContours(coppied, contour2, -1, (255, 0, 0), 8)

for c in contour:
    for p in c:
        cv2.circle(img, tuple(p[0]), 2, (0, 0, 255), -1)

for c in contour2:
    for p in c:
        cv2.circle(coppied, tuple(p[0]), 2, (0, 0, 255), -1)

cv2.putText(img, f'CHAIN_APPROX_NONE, Number of contours : {len(contour)}',
            (0, 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
cv2.putText(coppied, f'CHAIN_APPROX_SIMPLE, Number of contours : {len(contour2)}',
            (0, 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)

merged = np.vstack((img, coppied))

cv2.imshow('Contour', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()