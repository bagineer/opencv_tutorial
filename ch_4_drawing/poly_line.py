import cv2
import os
import os.path as osp
import numpy as np

## Settings
# Read image.
file_path = osp.dirname(osp.abspath(__file__))
file_path = osp.abspath(osp.join(file_path, os.pardir, 'ch_3_image_IO/captured'))
file_name = 'captured_002.png'
img_file = osp.join(file_path, file_name)
img = cv2.imread(img_file)

# poly line coordinates
tri = np.array([[200, 200], [300, 300], [400, 200]], np.int32)
quad = np.array([[100, 100], [400, 123], [453, 389], [217, 385]], np.int32)
penta = np.array([[384, 346], [294, 400], [123, 349], [28, 289], [396, 14]], np.int32)
hexa = np.array([[100, 100], [150, 50], [200, 100], [200, 200], [150, 350] ,[100, 300]], np.int32)
opened_quad = np.array([[50, 50], [300, 100], [270, 30], [500, 80]], np.int32)

if img is not None:

    # Draw poly lines
    cv2.polylines(img, [tri], True, (0, 0, 255))    # triangle
    cv2.polylines(img, [quad], True, (0, 255, 255), 2)    # quadrangle
    cv2.polylines(img, [penta], True, (255, 0, 255), 3)    # pentagon
    cv2.polylines(img, [hexa], True, (0, 255, 0), 4)    # hexagon
    cv2.polylines(img, [opened_quad], False, (255, 0, 0), 2)    # opened poly line
    cv2.imshow('Poly_lines', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('No image.')