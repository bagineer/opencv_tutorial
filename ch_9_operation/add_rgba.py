import cv2
import os.path as osp

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'sample.png'
img_file = osp.join(file_path, file_name)
img_fg = cv2.imread(img_file, cv2.IMREAD_UNCHANGED)
h, w, _ = img_fg.shape
img_file_2 = osp.join(file_path, 'lion.jpg')
img_fg = cv2.resize(img_fg, (w // 2, h // 2))
img_bg = cv2.imread(img_file_2)

_, mask = cv2.threshold(img_fg[:, :, 3], 1, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img_fg = cv2.cvtColor(img_fg, cv2.COLOR_BGRA2BGR)
h, w, _ = img_fg.shape
roi = img_bg[:h, :w]

print(h, w, roi.shape)

masked_fg = cv2.bitwise_and(img_fg, img_fg, None, mask)
masked_bg = cv2.bitwise_and(roi, roi, None, mask_inv)

added = masked_fg + masked_bg
img_bg[:h, :w] = added

cv2.imshow('img_fg', img_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()