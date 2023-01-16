import cv2
import os.path as osp

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'asdf.png'
img_file = osp.join(file_path, file_name)
img = cv2.imread(img_file)    # open color image.
# img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)    # open gray scale image.

if img is not None:
    cv2.imshow('Origin', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("No image files.")

