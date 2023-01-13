import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if cap.isOpened():
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    # fps = cap.get(cv2.CAP_PROP_FPS)
    fps = 30
    delay = int(1000/fps)

# MOG
fgbg1 = cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg2 = cv2.createBackgroundSubtractorMOG2()
while cap.isOpened():
    ret, frame = cap.read()
    if cv2.waitKey(delay) & 0xFF == 27 or not ret:
        break
    
    fgmask1 = fgbg1.apply(frame)
    fgmask1 = cv2.cvtColor(fgmask1, cv2.COLOR_GRAY2BGR)
    fgmask2 = fgbg1.apply(frame)
    fgmask2 = cv2.cvtColor(fgmask2, cv2.COLOR_GRAY2BGR)

    cv2.imshow('Webcam', frame)
    cv2.imshow('MOG1', fgmask1)
    cv2.imshow('MOG2 with shades', fgmask2)

cap.release()
cv2.destroyAllWindows()