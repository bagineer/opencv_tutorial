import cv2
import numpy as np

def lucas_kanade(frame, termcriteria, max_corners=200, quality_lv=0.01, min_dist=10):
    global prev_img, lines, prev_pts

    img_draw = frame.copy()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if prev_img is None:
        prev_img = img_gray
        lines = np.zeros_like(frame)
        prev_pts = cv2.goodFeaturesToTrack(prev_img, max_corners, quality_lv, min_dist)
    
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
            cv2.circle(img_draw, (nx, ny), 2, color[i].tolist(), -1)
        
        img_draw = cv2.add(img_draw, lines)
        prev_img = next_img
        prev_pts = next_move.reshape(-1, 1, 2)

    cv2.imshow('Optical Flow - LK', img_draw)

def draw_flow(frame, flow, step=16):
    h, w, _ = frame.shape
    idx_y, idx_x = np.mgrid[step/2:h:step, step/2:w:step].astype(np.int)
    indices = np.stack((idx_x, idx_y), axis=-1).reshape(-1, 2)

    for x, y in indices:
        cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
        dx, dy = flow[y, x].astype(np.int)
        cv2.line(frame, (x, y), (x+dx, y+dy), (0, 255, 0), 2, cv2.LINE_AA)

def gunner_farneback(frame, pyr_scale=0.5, levels=3, win_size=15, iterations=3, poly_n=5, poly_sigma=1.1):
    global prev_img2

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if prev_img2 is None:
        prev_img2 = img_gray
    else:
        flow = cv2.calcOpticalFlowFarneback(prev_img2, img_gray, None,
                                            pyr_scale, levels, win_size,
                                            iterations, poly_n, poly_sigma,
                                            cv2.OPTFLOW_FARNEBACK_GAUSSIAN)
        draw_flow(frame, flow)
        prev_img2 = img_gray

    cv2.imshow('Optical Flow - Farneback', frame)


cap = cv2.VideoCapture(0)
FPS = 30
DELAY = int(1000/(FPS*3))
MAX_CORNERS = 200

color = np.random.randint(0, 255, (MAX_CORNERS, 3))
prev_img, prev_img2 = None, None
next_img, next_pts, next_move = None, None, None
lines = None
termcriteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    lucas_kanade(frame, termcriteria, MAX_CORNERS, 0.01, 10)
    gunner_farneback(frame.copy())

    key = cv2.waitKey(DELAY) & 0xFF

    if key == 27:   # esc
        break
    elif key == 8:  # backspace
        prev_img = None

cap.release()
cv2.destroyAllWindows()