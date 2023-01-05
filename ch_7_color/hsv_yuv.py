import cv2 as cv
import numpy as np

r = np.array([[[0, 0, 255]]], dtype=np.uint8)
g = np.array([[[0, 255, 0]]], dtype=np.uint8)
b = np.array([[[255, 0, 0]]], dtype=np.uint8)
y = np.array([[[0, 255, 255]]], dtype=np.uint8)
k = np.array([[[0, 0, 0]]], dtype=np.uint8)
g = np.array([[[127, 127, 127]]], dtype=np.uint8)
w = np.array([[[255, 255, 255]]], dtype=np.uint8)

r_hsv = cv.cvtColor(r, cv.COLOR_BGR2HSV)
g_hsv = cv.cvtColor(g, cv.COLOR_BGR2HSV)
b_hsv = cv.cvtColor(b, cv.COLOR_BGR2HSV)
y_hsv = cv.cvtColor(y, cv.COLOR_BGR2HSV)
k_hsv = cv.cvtColor(k, cv.COLOR_BGR2HSV)
g_hsv = cv.cvtColor(g, cv.COLOR_BGR2HSV)
w_hsv = cv.cvtColor(w, cv.COLOR_BGR2HSV)

r_yuv = cv.cvtColor(r, cv.COLOR_BGR2YUV)
g_yuv = cv.cvtColor(g, cv.COLOR_BGR2YUV)
b_yuv = cv.cvtColor(b, cv.COLOR_BGR2YUV)
y_yuv = cv.cvtColor(y, cv.COLOR_BGR2YUV)
k_yuv = cv.cvtColor(k, cv.COLOR_BGR2YUV)
g_yuv = cv.cvtColor(g, cv.COLOR_BGR2YUV)
w_yuv = cv.cvtColor(w, cv.COLOR_BGR2YUV)

print('hsv')
print(r_hsv, g_hsv, b_hsv, y_hsv, k_hsv, g_hsv, w_hsv)
print()
print('yuv')
print(r_yuv, g_yuv, b_yuv, y_yuv, k_yuv, g_yuv, w_yuv)

# colored_image = np.zeros((10, 10, 3), dtype=np.uint8)
colored_image = np.full((100, 100, 3), cv.cvtColor(w_yuv, cv.COLOR_YUV2BGR), dtype=np.uint8)

cv.imshow('Color test', colored_image)
cv.waitKey(0)
cv.destroyAllWindows()