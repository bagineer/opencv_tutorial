import cv2
import numpy as np
import os.path as osp
from matplotlib import pyplot as plt

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'sample.jpg'
img_file = osp.join(file_path, file_name)
img = cv2.imread(img_file)
h, w, _ = img.shape

# Distort center
EXP, SCALE = 2, 1

mapy, mapx = np.indices((h, w), dtype=np.float32)
mapx, mapy = 2*mapx/(w - 1) - 1, 2*mapy/(h - 1) - 1

r, theta = cv2.cartToPolar(mapx, mapy)
r[r<SCALE] = r[r<SCALE]**EXP

mapx, mapy = cv2.polarToCart(r, theta)
mapx, mapy = (mapx + 1)*(w - 1)/2, (mapy + 1)*(h - 1)/2
distorted = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

cv2.imshow('Original', img)
cv2.imshow('Distorted', distorted)

# Distort Somewhere
dx, dy = 100, 100
normx, normy = max(dx, w - dx), max(dy, h - dy)
mapy, mapx = np.indices((h, w), dtype=np.float32)
mapx, mapy = (mapx - dx)/normx, (mapy - dy)/normy

r, theta = cv2.cartToPolar(mapx, mapy)
r[r<SCALE] = r[r<SCALE]**EXP

mapx, mapy = cv2.polarToCart(r, theta)
mapx, mapy = mapx*normx + dx, mapy*normy + dy
distorted = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

# Distort Anywhere
is_dragging = False
x0, y0 = -1, -1
mapx0, mapy0 = None, None
exp = 1
distorted = img.copy()

def distort(img, x, y):
    global mapx0, mapy0, distorted

    h, w, _ = img.shape
    norm_x, norm_y = max(x, w - x), max(y, h - y)
    mapy, mapx = np.indices((h, w), dtype=np.float32)
    
    mapx, mapy = (mapx - x) / norm_x, (mapy - y) / norm_y
    r, theta = cv2.cartToPolar(mapx, mapy)
    r[r<SCALE] = r[r<SCALE]**exp

    mapx, mapy = cv2.polarToCart(r, theta)
    mapx0, mapy0 = mapx*norm_x + x, mapy*norm_y + y
    distorted = cv2.remap(img, mapx0, mapy0, cv2.INTER_LINEAR)
    cv2.imshow(win_name, distorted)

def onMouse(event, x, y, flag, param):
    global x0, y0, is_dragging
    if event == cv2.EVENT_LBUTTONDOWN:
        is_dragging = True
        x0, y0 = x, y
        distort(img, x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if is_dragging:
            x0, y0 = x, y
            distort(img, x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        if is_dragging:
            is_dragging = False

def onChange(x):
    global exp
    exp = (x + 5) / 10
    distort(img, x0, y0)
    cv2.imshow(win_name, distorted)

win_name = 'Distort Anywhere'
cv2.namedWindow(win_name)
cv2.setMouseCallback(win_name, onMouse)
cv2.createTrackbar('EXP', win_name, 5, 15, onChange)
cv2.imshow(win_name, img)

# barrel and pincushion distortion
k11, k12, k13 = 0.5, 0.2, 0.0
k21, k22, k23 = -0.3, 0, 0

mapy, mapx = np.indices((h, w), dtype=np.float32)
mapx = 2*mapx/(w-1) - 1
mapy = 2*mapy/(h-1) - 1
r, theta = cv2.cartToPolar(mapx, mapy)

ru1 = r*(1 + k11*(r**2) + k12*(r**4) + k13*(r**6))
ru2 = r*(1 + k21*(r**2) + k22*(r**4) + k23*(r**6))

mapx1, mapy1 = cv2.polarToCart(ru1, theta)
mapx2, mapy2 = cv2.polarToCart(ru2, theta)
mapx1, mapy1 = (mapx1+1)*(w-1)/2, (mapy1+1)*(h-1)/2
mapx2, mapy2 = (mapx2+1)*(w-1)/2, (mapy2+1)*(h-1)/2

distorted1 = cv2.remap(img, mapx1, mapy1, cv2.INTER_LINEAR)
distorted2 = cv2.remap(img, mapx2, mapy2, cv2.INTER_LINEAR)

plt.subplot(121)
plt.imshow(distorted1)
plt.title('Barrel')
plt.axis('off')
plt.subplot(122)
plt.imshow(distorted2)
plt.title('Barrel')
plt.axis('off')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()