import cv2
import numpy as np

img = cv2.imread('./sample.jpg')

kernel = np.ones((5, 5)) / 25
blurred = cv2.filter2D(img, -1, kernel)

cv2.imshow('Original', img)
cv2.imshow('Blurred', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()