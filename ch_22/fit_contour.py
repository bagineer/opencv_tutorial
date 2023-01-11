import cv2
import numpy as np

win_name = 'Fit Contour'
img = np.ones((400, 400), np.uint8)*255
draw = img.copy()
is_dragging = False
pts = list()

def onMouse(event, x, y, flags, param):
    global is_dragging, draw

    if event == cv2.EVENT_LBUTTONDOWN:
        pts.append([x, y])
        cv2.circle(draw, (x, y), 2, 0, -1)
        cv2.imshow(win_name, draw)
        print(pts)

    elif event == cv2.EVENT_MOUSEMOVE:
        pass

    elif event == cv2.EVENT_LBUTTONUP:
        pass

cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)

while True:
    key = cv2.waitKey(1)
    if key == 13:
        cv2.fillPoly(img, [np.array(pts)], 0)
        cv2.imshow(win_name, img)
    if key == 27:
        break

cv2.destroyAllWindows()