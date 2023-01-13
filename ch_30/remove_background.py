import cv2
import numpy as np

cap = cv2.VideoCapture(0)
win_name = 'Remove Background'

if cap.isOpened():
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    # fps = cap.get(cv2.CAP_PROP_FPS)
    fps = 30
    delay = int(1000/fps)

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
while cap.isOpened():
    ret, frame = cap.read()
    if cv2.waitKey(delay) & 0xFF == 27 or not ret:
        break
    
    fgmask = fgbg.apply(frame)
    fgmask = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR)
    cv2.imshow(win_name, np.hstack((frame, fgmask)))

cap.release()
cv2.destroyAllWindows()