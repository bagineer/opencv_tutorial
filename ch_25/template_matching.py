import cv2
import os.path as osp

file_path = osp.dirname(osp.abspath(__file__))
img_match = osp.join(file_path, 'figures.jpg')
img_template = osp.join(file_path, 'taekwonv3.jpg')
matching = cv2.imread(img_match)
template = cv2.imread(img_template)
th, tw, _ = template.shape
win_name = 'Template Matching'

cv2.imshow(win_name, template)

methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF_NORMED']

for i, method_name in enumerate(methods):
    img_draw = matching.copy()
    method = eval(method_name)
    res = cv2.matchTemplate(matching, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(method, min_val, max_val, min_loc, max_loc)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left, match_val = min_loc, min_val
    else:
        top_left, match_val = max_loc, max_val
    bottom_right = (top_left[0] + tw, top_left[1] + th)
    cv2.rectangle(img_draw, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(img_draw, str(match_val), top_left,
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1, cv2.LINE_AA)

    cv2.imshow(method_name, img_draw)

cv2.waitKey()
cv2.destroyAllWindows()