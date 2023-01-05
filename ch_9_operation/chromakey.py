import cv2
import numpy as np
from matplotlib import pyplot as plt

fg = cv2.imread('./chromakey.jpg')
fg = fg[50:-50]
bg = cv2.imread('./antarctica.jpg')

h, w, _ = fg.shape
h2, w2, _ = bg.shape
x = (w2 - w)//2
y = (h2 - h)//2

chromakey = fg[100:110, 100:110, :]
offset = 20

hsv_chroma = cv2.cvtColor(chromakey, cv2.COLOR_BGR2HSV)
hsv_fg = cv2.cvtColor(fg, cv2.COLOR_BGR2HSV)

color = hsv_chroma[:, :, 0]
lower = np.array([color.min() - offset, 100, 100])
upper = np.array([color.max() + offset, 255, 255])

mask = cv2.inRange(hsv_fg, lower, upper)
mask_inv = cv2.bitwise_not(mask)

roi = bg[y:y+h, x:x+w]
fg_img = cv2.bitwise_and(fg, fg, None, mask_inv)
bg_img = cv2.bitwise_and(roi, roi, None, mask)
orig = bg.copy()
bg[y:y+h, x:x+w] = fg_img + bg_img

cv2.imshow('original', orig)
cv2.imshow('chromakey', fg)
cv2.imshow('added', bg)

cv2.waitKey()
cv2.destroyAllWindows()