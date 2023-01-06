import cv2
import numpy as np
from matplotlib import pyplot as plt

win_name = 'Back projection'
# img = cv2.imread('./sample.jpeg')
img = cv2.imread('./sample2.jpg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
draw = img.copy()

def masking(bp, win_name, i):
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    cv2.filter2D(bp, -1, disc, bp)
    cv2.imwrite(f'./mask_before_thresholding.png', bp)

    _, mask = cv2.threshold(bp, 1, 255, cv2.THRESH_BINARY)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow(win_name, result)
    cv2.imwrite(f'./mask_{i}.png', mask)

def backProject_manual(hist_roi):
    hist_img = cv2.calcHist([hsv_img], [0, 1], None, [180, 256], [0, 180, 0, 256])
    hist_rate = hist_roi / (hist_img + 1)

    plt.figure('original')
    plt.style.use('classic')
    p = plt.imshow(hist_img)
    plt.title('original')
    plt.xlabel('S')
    plt.ylabel('H', rotation=0)
    plt.colorbar(p)
    plt.savefig('./original.png')

    plt.figure('ROI')
    p = plt.imshow(hist_roi)
    plt.title('ROI')
    plt.xlabel('S')
    plt.ylabel('H', rotation=0)
    plt.colorbar(p)
    plt.savefig('./roi.png')

    plt.figure('Rate')
    p = plt.imshow(hist_rate)
    plt.title('Rate')
    plt.xlabel('S')
    plt.ylabel('H', rotation=0)
    plt.colorbar(p)
    plt.savefig('./hist_rate.png')

    h, s, v = cv2.split(hsv_img)
    bp = hist_rate[h.ravel(), s.ravel()]
    bp = bp.reshape(hsv_img.shape[:2])

    plt.figure('bp')
    p = plt.imshow(bp)
    plt.title('bp')
    plt.xlabel('X')
    plt.ylabel('Y', rotation=0)
    plt.colorbar(p)
    plt.savefig('./bp.png')

    cv2.normalize(bp, bp, 0, 255, cv2.NORM_MINMAX)
    bp = bp.astype(np.uint8)

    # print(set(bp.ravel()))
    masking(bp, 'result_manual', 1)

def backProject_cv(hist_roi):
    bp = cv2.calcBackProject([hsv_img], [0, 1], hist_roi, [0, 180, 0, 256], 1)
    # print(len(set(bp.ravel())))
    masking(bp, 'result_cv', 2)

(x, y, w, h) = cv2.selectROI(win_name, img, False)
if w > 0 and h > 0:
    roi = draw[y:y+h, x:x+w]
    cv2.rectangle(draw, (x, y), (x+w, y+h), (0, 0, 255), 2)
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    hist_roi = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
    backProject_manual(hist_roi)
    backProject_cv(hist_roi)

plt.show()
cv2.imshow(win_name, draw)
cv2.waitKey()
cv2.destroyAllWindows()