import cv2

win_name = "Mosaic with Blurring"
ksize = 20

img = cv2.imread('./sample.jpg')
cv2.imshow(win_name, img)

while True:
    x, y, w, h = cv2.selectROI(win_name, img, False)
    if w > 0 and h > 0:
        roi = img[y:y+h, x:x+w]
        roi = cv2.blur(roi, (ksize, ksize))
        img[y:y+h, x:x+w] = roi
        cv2.imshow(win_name, img)
    else:
        break
cv2.destroyAllWindows()