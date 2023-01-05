import cv2 as cv
import os.path as osp

file_name = 'sample.jpg'
image = cv.imread(file_name)
title = 'ROI'
HEIGHT, WIDTH, _ = image.shape
SCALE = 0.2

cv.namedWindow(title)
print(WIDTH, HEIGHT)


if image is not None:
    resized = cv.resize(image, (int(WIDTH*SCALE), int(HEIGHT*SCALE)))
    height, width, _ = resized.shape
    # print(width, height)

    # roi
    x, y, w, h = 425, 0, 300, 650
    roi = resized[y:y+h, x:x+w].copy()
    cv.rectangle(resized, (x, y), (x+w, y+h), (0, 0, 255), 2)
    resized[height-h:, width-w:] = roi

    cv.imshow('roi', roi)
    cv.imwrite('./roi.jpg', roi)

    cv.imshow(title, resized)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    exit(-1)