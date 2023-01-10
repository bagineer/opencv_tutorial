import cv2
import numpy as np

img = cv2.imread('./sample.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (400, 300), interpolation=cv2.INTER_LINEAR)
# ret, img = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
cv2.imshow('Original', img)

# Erosion and Dilation
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
eroded = cv2.erode(img, k)
dilated = cv2.dilate(img, k)
merged = np.hstack((eroded, dilated))
cv2.imshow('Erosion and Dilation', merged)

# Open and Close
opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, k)
closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, k)
merged = np.hstack((opened, closed))
cv2.imshow('Open and Close', merged)

# Morphology gradient
grad1 = dilated - eroded
grad2 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k)
merged = np.hstack((grad1, grad2))
cv2.imshow('Gradient', merged)

# Top hat and Black hat
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, k)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, k)
merged = np.hstack((tophat, blackhat))
cv2.imshow('Top hat and Black hat', merged)

cv2.waitKey(0)
cv2.destroyAllWindows()