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

def get_contours(img, mode, method):
    _, img_bin = cv2.threshold(img[:, :, 0], 127, 255, cv2.THRESH_BINARY_INV)
    _, contours, _ = cv2.findContours(img_bin, mode, method)
    return contours[0]

def fit_contour_bound(img):
    contour = get_contours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

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
    h, w, _ = img.shape
    cv2.line(img, (0, 0-x*(vy/vx) + y), (w-1, (w-x)*(vy/vx) + y), (0, 255, 255), 4)

def simplify_contour(img, e):
    contour = get_contours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    epsilon = e * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # draw contour
    cv2.drawContours(img, [contour], -1, (0, 0, 255), 4)
    cv2.drawContours(img, [approx], -1, (0, 255, 0), 4)

def convex_hull(img):
    contour = get_contours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img, [contour], -1, (0, 0, 255), 4)

    hull = cv2.convexHull(contour)
    cv2.drawContours(draw, [hull], -1, (0, 255, 0), 4)

    hull2 = cv2.convexHull(contour, returnPoints=False)
    defects = cv2.convexityDefects(contour, hull2)

    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        farthest = tuple(contour[f][0])
        dist = d/256.0
        if dist > 1:
            cv2.circle(draw, farthest, 4, (255, 0, 0), -1)
        

cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)

while cv2.getWindowProperty(win_name, 0) >= 0:
    key = cv2.waitKey(1)

    if key == 13:   # enter
        cv2.fillPoly(img, [np.array(pts)], 0)
        cv2.imshow(win_name, img)
        draw = img.copy()
    
    elif key == 27:   # esc
        break

    elif key == ord('c'):
        cv2.imshow(win_name, origin)
        pts = list()
        draw = origin.copy()
        img = origin.copy()
    
    elif key == ord('f'):
        fit_contour_bound(draw)
        cv2.imshow(win_name, draw)
    
    elif key == ord('s'):
        simplify_contour(draw, 0.05)
        cv2.imshow(win_name, draw)

    elif key == ord('h'):
        convex_hull(draw)
        cv2.imshow(win_name, draw)

cv2.destroyAllWindows()