import cv2
import os.path as osp

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'cmes.png'
img_file = osp.join(file_path, file_name)
img = cv2.imread(img_file)
h, w, _ = img.shape
SCALE = 0.5

dst1 = cv2.resize(img, (int(w*SCALE), int(h*SCALE)),
                    interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(img, None, None, SCALE, SCALE, cv2.INTER_CUBIC)

cv2.imshow('Original', img)
cv2.imshow('dsize', dst1)
cv2.imshow('fxfy', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()