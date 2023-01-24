import cv2
import os.path as osp

win_name = "Mosaic with Blurring"
ksize = 20

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'sample.jpg'
img_file = osp.join(file_path, file_name)
img = cv2.imread(img_file)
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