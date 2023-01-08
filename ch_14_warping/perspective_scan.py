import cv2
import numpy as np

win_name = 'Scanning'
img = cv2.imread('./leaflet.jpg')
h, w, _ = img.shape
draw = img.copy()
pts_cnt = 0
pts = np.zeros((4, 2), dtype=np.float32)

def onMouse(event, x, y, flag, param):
    global pts_cnt
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(draw, (x, y), 10, (0, 0, 255), -1)
        cv2.imshow(win_name, draw)

        pts[pts_cnt] = [x, y]
        pts_cnt += 1

        if pts_cnt > 3:
            pts_sum = pts.sum(axis=1)
            diff = np.diff(pts, axis=1)

            tl = pts[np.argmin(pts_sum)]
            br = pts[np.argmax(pts_sum)]
            tr = pts[np.argmin(diff)]
            bl = pts[np.argmax(diff)]

            pts1 = np.float32([tl, tr, br, bl])

            w1 = abs(br[0] - bl[0])
            w2 = abs(tr[0] - tl[0])
            h1 = abs(tr[1] - br[1])
            h2 = abs(tl[1] - bl[1])
            
            width, height = max(w1, w2), max(h1, h2)

            pts2 = np.float32([[0, 0], [width-1, 0], [width-1, height-1], [0, height-1]])

            m = cv2.getPerspectiveTransform(pts1, pts2)
            res = cv2.warpPerspective(img, m, (width, height))
            cv2.imshow('Scanned', res)

cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()