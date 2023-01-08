import cv2
import numpy as np

img = cv2.imread('./cmes.png')
img = cv2.resize(img, (512, 512))
h, w, _ = img.shape

s, b = 0.3, 1.7
Ms = np.float32([[s, 0, 0],
                 [0, s, 0]])
Mb = np.float32([[b, 0, 0],
                 [0, b, 0]])

dst1 = cv2.warpAffine(img, Ms, (int(h*s), int(w*s)))
dst2 = cv2.warpAffine(img, Mb, (int(h*b), int(w*b)))
dst3 = cv2.warpAffine(img, Ms, (int(h*s), int(w*s)), None, cv2.INTER_AREA)
dst4 = cv2.warpAffine(img, Mb, (int(h*b), int(w*b)), None, cv2.INTER_CUBIC)

cv2.imshow('Original', img)
cv2.imshow('Small', dst1)
cv2.imshow('Big', dst2)
cv2.imshow('Small INTER_AREA', dst3)
cv2.imshow('Big INTER_CUBIC', dst4)
cv2.waitKey(0)
cv2.destroyAllWindows()