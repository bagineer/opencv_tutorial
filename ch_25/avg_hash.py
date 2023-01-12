import cv2
import numpy as np
import glob

img = cv2.imread('./pistol.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.resize(img_gray, (16, 16))
mean = gray.mean()

binary = 1 * (gray > mean)

dhash = []
for row in binary.tolist():
    s = ''.join([str(i) for i in row])
    dhash.append('%02x'%(int(s,2)))
dhash = ''.join(dhash)

cv2.putText(img, dhash, (10, 20), cv2.FONT_HERSHEY_PLAIN,
            0.6, (0, 0, 255), 1)
cv2.imshow('Image', img)
cv2.waitKey()
cv2.destroyAllWindows()