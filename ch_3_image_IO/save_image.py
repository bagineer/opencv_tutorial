import cv2
import os.path as osp

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'asdf.png'
img_file = osp.join(file_path, file_name)
gray_img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if gray_img is not None:
    cv2.imwrite(osp.join(file_path, 'gray_scale.png'), gray_img)
    cv2.destroyAllWindows()
else:
    print('no image files.')