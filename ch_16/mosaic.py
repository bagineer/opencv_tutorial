import cv2

rate = 10
win_name = 'Mosaic'
img = cv2.imread('./sample.jpg')

while True:
    x, y, w, h = cv2.selectROI(win_name, img, False)
    if w and h:
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (w//rate, h//rate))

        roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_AREA)
        img[y:y+h, x:x+w] = roi
        cv2.imshow(win_name, roi)
    else:
        break
cv2.destroyAllWindows()