import cv2
import os.path as osp

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'sample.jpg'
img_file = osp.join(file_path, file_name)
image = cv2.imread(img_file)
title = 'ROI'
HEIGHT, WIDTH, _ = image.shape
SCALE = 0.2

cv2.namedWindow(title)
print(WIDTH, HEIGHT)


if image is not None:
    resized = cv2.resize(image, (int(WIDTH*SCALE), int(HEIGHT*SCALE)))
    height, width, _ = resized.shape
    # print(width, height)

    # roi
    x, y, w, h = 425, 0, 300, 650
    roi = resized[y:y+h, x:x+w].copy()
    cv2.rectangle(resized, (x, y), (x+w, y+h), (0, 0, 255), 2)
    resized[height-h:, width-w:] = roi

    cv2.imshow('roi', roi)
    cv2.imwrite(osp.join(file_path, 'roi.jpg'), roi)

    cv2.imshow(title, resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    exit(-1)