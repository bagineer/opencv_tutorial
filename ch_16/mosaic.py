import cv2
import os.path as osp

def onChange(r):
    global rate, draw
    rate = (r+1) * 5
    if w > 0 and h > 0:
        draw = mosaic(img.copy(), x, y, w, h, rate)

def mosaic(draw, x, y, w, h, rate):
    roi = draw[y:y+h, x:x+w]
    roi = cv2.resize(roi, (w//rate, h//rate))
    roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_AREA)
    draw[y:y+h, x:x+w] = roi
    cv2.imshow(win_name, draw)
    return draw

rate = 10
win_name = 'Mosaic'
file_path = osp.dirname(osp.abspath(__file__))
file_name = 'sudoku.jpg'
img_file = osp.join(file_path, file_name)
img = cv2.imread(img_file)
draw = img.copy()
x, y, w, h = -1, -1, -1, -1

cv2.namedWindow(win_name)
cv2.createTrackbar('rate', win_name, 0, 4, onChange)

while True:
    x, y, w, h = cv2.selectROI(win_name, draw, False)
    if w and h:
        draw = mosaic(img.copy(), x, y, w, h, rate)
    else:
        break
cv2.destroyAllWindows()