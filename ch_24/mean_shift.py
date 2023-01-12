import cv2
import numpy as np

img = cv2.imread('./cool.jpg')
win_name = 'Mean Shift'
tb1_name = 'SP'
tb2_name = 'SR'
tb3_name = 'LV'

def onChange(x):
    sp = cv2.getTrackbarPos(tb1_name, win_name)
    sr = cv2.getTrackbarPos(tb2_name, win_name)
    lv = cv2.getTrackbarPos(tb3_name, win_name)

    mean = cv2.pyrMeanShiftFiltering(img, sp, sr, None, lv)

    cv2.imshow(win_name, np.hstack((img, mean)))

cv2.imshow(win_name, np.hstack((img, img)))
cv2.createTrackbar(tb1_name, win_name, 10, 100, onChange)
cv2.createTrackbar(tb2_name, win_name, 10, 100, onChange)
cv2.createTrackbar(tb3_name, win_name, 2, 5, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()