import cv2
import numpy as np

cap = cv2.VideoCapture(0)
WIDTH, HEIGHT = 640, 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

while cap.isOpened():
    ret, frame = cap.read()

    blurred = cv2.blur(frame, (5, 5))
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    laplacian = cv2.Laplacian(gray, -1, None, 5)

    _, edge = cv2.threshold(laplacian, 50, 255, cv2.THRESH_BINARY_INV)
    edge = cv2.morphologyEx(edge, cv2.MORPH_CLOSE, (3, 3))
    edge = cv2.medianBlur(edge, 3)

    img_paint = cv2.bitwise_and(blurred, blurred, mask=edge)
    merged = np.hstack((frame, img_paint))

    if cv2.waitKey(1) & 0xFF == 27: break
    cv2.imshow('Recording', merged)

cap.release()
cv2.destroyAllWindows()