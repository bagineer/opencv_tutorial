import cv2
import numpy as np

win_name = 'Fit Contour'
origin = np.ones((400, 400, 3), np.uint8)*255
img = origin.copy()
draw = origin.copy()
is_dragging = False
pts = list()

def onMouse(event, x, y, flags, param):
    global is_dragging, draw

    if event == cv2.EVENT_LBUTTONDOWN:
        pts.append([x, y])
        cv2.circle(draw, (x, y), 2, 0, -1)
        cv2.imshow(win_name, draw)

    elif event == cv2.EVENT_MOUSEMOVE:
        pass

    elif event == cv2.EVENT_LBUTTONUP:
        pass

def fit_contour_bound(img):
    _, img_bin = cv2.threshold(img[:, :, 0], 127, 255, cv2.THRESH_BINARY_INV)
    _, contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = contours[0]

    # draw bounding rectangle
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 4)

    # draw minimal rectangle
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img, [box], -1, (0, 255, 0), 4)

    # draw minimal circle
    (x, y), r = cv2.minEnclosingCircle(contour)
    cv2.circle(img, (int(x), int(y)), int(r), (255, 0, 0), 4)

    # draw minimal triangle
    _, tri = cv2.minEnclosingTriangle(contour)
    cv2.polylines(img, [np.int32(tri)], True, (255, 255, 0), 4)

    # draw minimal ellipse
    ellipse = cv2.fitEllipse(contour)
    cv2.ellipse(img, ellipse, (255, 0, 255), 4)

    # draw centerline
    [vx, vy, x, y] = cv2.fitLine(contour, cv2.DIST_L2, 0, 0.01, 0.01)
    h, w = img_bin.shape
    cv2.line(img, (0, 0-x*(vy/vx) + y), (w-1, (w-x)*(vy/vx) + y), (0, 255, 255), 4)

cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)

while cv2.getWindowProperty(win_name, 0) >= 0:
    key = cv2.waitKey(1)
    if key == 13:   # enter
        cv2.fillPoly(img, [np.array(pts)], 0)
        cv2.imshow(win_name, img)
    elif key == 27:   # esc
        break
    elif key == ord('c'):
        cv2.imshow(win_name, origin)
        pts = list()
        draw = origin.copy()
        img = origin.copy()
    elif key == ord('f'):
        fit_contour_bound(img)
        cv2.imshow(win_name, img)

cv2.destroyAllWindows()