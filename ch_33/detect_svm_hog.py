import cv2

hog_default = cv2.HOGDescriptor()
hog_default.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

hog_daimler = cv2.HOGDescriptor((48, 96), (16, 16), (8, 8), (8, 8), 9)
hog_daimler.setSVMDetector(cv2.HOGDescriptor_getDaimlerPeopleDetector())

cap = cv2.VideoCapture(0)
mode = True
hog_name = ['Daimler', 'Default']

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if mode:
        found, _ = hog_default.detectMultiScale(frame)
        for (x, y, w, h) in found:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255))
    else:
        found, _ = hog_daimler.detectMultiScale(frame)
        for (x, y, w, h) in found:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0))
    cv2.putText(frame, f'Detector : {hog_name[mode]}', (20, 20),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('Frame', frame)

    key = cv2.waitKey(1) & 0xff
    if key == 27:
        break
    elif key == ord(' '):
        mode = not mode

cap.release()
cv2.destroyAllWindows()