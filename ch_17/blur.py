import cv2
import numpy as np

img = cv2.imread('./sample.jpg')
h, w, b = img.shape
noised = img + np.random.randint(-30, 30, (h, w, b))
noised[noised<0] = 0
noised[noised>255] = 255
noised = noised.astype(np.uint8)

# Average Blurring
kernel = np.ones((5, 5)) / 25
blurred = cv2.filter2D(img, -1, kernel)

# cv2.blur
blur1 = cv2.blur(img, (7, 7))
blur2 = cv2.boxFilter(img, -1, (9, 9))

# Gaussian
k1 = np.array([[1, 2, 1],
               [2, 4, 2],
               [1, 2, 1]])/16
blur3 = cv2.filter2D(noised, -1, k1)

k2 = cv2.getGaussianKernel(3, 0)
blur4 = cv2.filter2D(noised, -1, k2*k2.T)

blur5 = cv2.GaussianBlur(noised, (3, 3), 0)

gaussian1 = np.hstack((noised, blur3))
gaussian2 = np.hstack((blur4, blur5))
gaussian_blur = np.vstack((gaussian1, gaussian2))

# Median blur
median = cv2.medianBlur(img, 3)
median_blur = np.hstack((noised, median))

# Bilateral
bilateral = cv2.bilateralFilter(img, 5, 80, 80)

cv2.imshow('Original', img)
cv2.imshow('Blurred', blurred)
cv2.imshow('cv2.blur', blur1)
cv2.imshow('cv2.boxFilter', blur2)
cv2.imshow('Gaussian', gaussian_blur)
cv2.imshow('Median', median_blur)
cv2.imshow('Bilateral', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()