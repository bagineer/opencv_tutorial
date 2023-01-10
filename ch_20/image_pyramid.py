import cv2
import numpy as np

img = cv2.imread('./sample.jpg')
cv2.imshow('Original', img)
h, w, _ = img.shape
img = cv2.resize(img, (h-1, w-1))

# Gaussian Pyramid
smaller = cv2.pyrDown(img)
bigger = cv2.pyrUp(img)
gaussian_title = 'Gaussian'

cv2.imshow(f'{gaussian_title} Smaller', bigger)
cv2.imshow(f'{gaussian_title} Bigger', smaller)

# Laplacian
blurred = cv2.pyrUp(smaller)
laplacian = cv2.subtract(img, blurred)
restored = blurred + laplacian

merged1 = np.hstack((img, blurred))
merged2 = np.hstack((laplacian, restored))
merged = np.vstack((merged1, merged2))
cv2.imshow('Laplacian', merged)

cv2.waitKey(0)
cv2.destroyAllWindows()