import cv2
import numpy as np

img = cv2.imread('./sample.jpg')
h, w, _ = img.shape
win_name = 'Painting'

mask = np.zeros((h+2, w+2), np.uint8)
dye = [0, 255, 255]
lower_diff, upper_diff = (10, 10, 10), (10, 10, 10)

def onMouse(event, x, y, flags, param):
    global mask, img
    if event == cv2.EVENT_LBUTTONDOWN:
        seed = (x, y)
        cv2.floodFill(img, mask ,seed, dye, lower_diff, upper_diff)
        cv2.imshow(win_name, img)

cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)
cv2.waitKey()
cv2.destroyAllWindows()