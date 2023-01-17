import cv2
import os.path as osp

# Read image.
file_path = osp.dirname(osp.abspath(__file__))
file_name = 'sample.jpg'
img_file = osp.join(file_path, file_name)
image = cv2.imread(img_file)

# Resize image.
HEIGHT, WIDTH, _ = image.shape
SCALE = 0.2
image = cv2.resize(image, (int(WIDTH*SCALE), int(HEIGHT*SCALE)))

if image is not None:
    cv2.imshow('Select ROI', image)

    while True:
        if cv2.waitKey(0) == ord('q'):
            cv2.destroyAllWindows()
            break

        x, y, w, h = cv2.selectROI('Select ROI', image)
        if w and h:
            roi = image[y:y+h, x:x+w]
            cv2.imshow('ROI', roi)
else:
    exit(-1)
