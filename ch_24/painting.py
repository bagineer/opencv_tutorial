import cv2
import numpy as np

img = cv2.imread('./sample.jpg')
origin = img.copy()
img_draw = img.copy()
h, w, _ = img.shape
win_name = 'Painting'

# Flood Fill
mask = np.zeros((h+2, w+2), np.uint8)
dye = [0, 255, 255]
lower_diff, upper_diff = (10, 10, 10), (10, 10, 10)

def onMouse(event, x, y, flags, param):
    global mask, img, img_draw, marker, marker_id, is_dragging
    if event == cv2.EVENT_LBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_CTRLKEY:
            seed = (x, y)
            cv2.floodFill(img, mask ,seed, dye, lower_diff, upper_diff)
            cv2.imshow(win_name, img)
        else:
            is_dragging = True
            colors.append((marker_id, img[y, x]))

    elif event == cv2.EVENT_MOUSEMOVE:
        if is_dragging:
            marker[y, x] = marker_id
            cv2.circle(img_draw, (x, y), 3, (0, 0, 255), -1)
            cv2.imshow(win_name, img_draw)
    
    elif event == cv2.EVENT_LBUTTONUP:
        if is_dragging:
            is_dragging = False
            marker_id += 1

# Watershed
marker = np.zeros((h, w), np.int32)
marker_id = 1
colors = []
is_dragging = False


cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)

while True:
    key =  cv2.waitKey(1)
    if key == 27:   # esc
        break
    elif key == 13: # enter
        cv2.watershed(img, marker)
        img_draw[marker == -1] = (0, 255, 0)
        for mid, color in colors:
            img_draw[marker == mid] = color
        cv2.imshow(win_name, img_draw)
    elif key == ord('c'):
        img_draw = origin.copy()
        img = origin.copy()
        marker = np.zeros((h, w), np.int32)
        marker_id = 1
        colors = []
        mask = np.zeros((h+2, w+2), np.uint8)
        cv2.imshow(win_name, origin)

cv2.destroyAllWindows()