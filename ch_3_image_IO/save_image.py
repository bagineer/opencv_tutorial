from re import L
import cv2

img_file = './asdf.png'
gray_img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if gray_img is not None:
    cv2.imwrite('./gray_scale.png', gray_img)
    cv2.destroyAllWindows()
else:
    print('no image files.')