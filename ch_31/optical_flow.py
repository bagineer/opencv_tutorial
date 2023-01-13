import cv2
import numpy as np

cap = cv2.VideoCapture(0)
FPS = 30
DELAY = int(1000/FPS)
MAX_CORNERS = 200

color = np.random.randint(0, 255, (MAX_CORNERS, 3))
lines = None
prev_img = None
termcriteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    img_draw = frame.copy()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if prev_img is None:
        prev_img = img_gray
        lines = np.zeros_like(frame)
        prev_pts = cv2.goodFeaturesToTrack(prev_img, MAX_CORNERS, 0.01, 10)

    else:
        next_img = img_gray
        next_pts, status, err = cv2.calcOpticalFlowPyrLK(prev_img, next_img,
                                                         prev_pts, None, criteria=termcriteria)
        prev_move = prev_pts[status==1]
        next_move = next_pts[status==1]

        for i, (p, n) in enumerate(zip(prev_move, next_move)):
            px, py = p.ravel()
            nx, ny = n.ravel()

            cv2.line(lines, (px, py), (nx, ny), color[i].tolist(), 2)
            cv2.circle(img_draw, (nx, ny), 1, color[i].tolist(), -1)
        
        img_draw = cv2.add(img_draw, lines)
        prev_img = next_img
        prev_pts = next_move.reshape(-1, 1, 2)
    
    cv2.imshow('Optical Flow - LK', img_draw)
    key = cv2.waitKey(DELAY) & 0xFF

    if key == 27:   # esc
        break
    elif key == 8:  # backspace
        prev_img = None

cap.release()
cv2.destroyAllWindows()