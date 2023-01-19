import cv2
import os.path as osp

win_name = 'Alpha Blending'
tb_name = 'Fade'

def onChange(x):
    alpha = x/100
    blended = cv2.addWeighted(img1, alpha, img2, 1-alpha, 0)
    cv2.imshow(win_name, blended)

file_path = osp.dirname(osp.abspath(__file__))
img_file1 = osp.join(file_path, 'lion.jpg')
img_file2 = osp.join(file_path, 'tiger.jpg')
img1 = cv2.imread(img_file1)
img2 = cv2.imread(img_file2)
h1, w1, _ = img1.shape
h2, w2, _ = img2.shape
mh, mw = min(h1, h2), min(w1, w2)
dh, dw = h1 - mh, w2 - mw
img1 = img1[dh//2:dh//2+mh, dw//2:dw//2+mw, :]  # crop bigger image by small image sizes

cv2.imshow(win_name, img2)
cv2.createTrackbar(tb_name, win_name, 0, 100, onChange)

cv2.waitKey(0)
cv2.destroyAllWindows()