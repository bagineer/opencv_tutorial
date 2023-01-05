import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./sample.png')

# hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

rl, rr = np.array([0, 50,50]), np.array([15, 255,255])
gl, gr = np.array([45, 50,50]), np.array([75, 255,255])
bl, br = np.array([90, 50, 50]), np.array([120, 255,255])
yl, yr = np.array([20, 50,50]), np.array([35, 255,255])

rmask = cv2.inRange(hsv, rl, rr)
gmask = cv2.inRange(hsv, gl, gr)
bmask = cv2.inRange(hsv, bl, br)
ymask = cv2.inRange(hsv, yl, yr)


# bgr
# t = 255
# l = (0, 0, 0)
# rr = (0, 0, t)
# gr = (0, t, 0)
# br = (t, 0, 0)
# yr = (0, t, t)

# rmask = cv2.inRange(img, l, rr)
# gmask = cv2.inRange(img, l, gr)
# bmask = cv2.inRange(img, l, br)
# ymask = cv2.inRange(img, l, yr)

res_r = cv2.bitwise_and(img, img, None, rmask)
res_g = cv2.bitwise_and(img, img, None, gmask)
res_b = cv2.bitwise_and(img, img, None, bmask)
res_y = cv2.bitwise_and(img, img, None, ymask)

imgs = {'original': img, 'red': res_r, 'green': res_g,
        'blue': res_b, 'yellow': res_y}

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(3, 2, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)
    plt.xticks([])
    plt.yticks([])
plt.show()