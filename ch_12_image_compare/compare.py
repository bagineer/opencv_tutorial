import cv2
import numpy as np
import os.path as osp
from matplotlib import pyplot as plt

file_path = osp.dirname(osp.abspath(__file__))
img_file1 = osp.join(file_path, 'taekwonv1.jpg')
img_file2 = osp.join(file_path, 'taekwonv2.jpg')
img_file3 = osp.join(file_path, 'taekwonv3.jpg')
img_file4 = osp.join(file_path, 'dr_ochanomizu.jpg')
img1 = cv2.imread(img_file1)
img2 = cv2.imread(img_file2)
img3 = cv2.imread(img_file3)
img4 = cv2.imread(img_file4)

win_name = 'Query'
cv2.imshow(win_name, img1)
imgs = [img1, img2, img3, img4]
hists = []

for i, img in enumerate(imgs):
    plt.subplot(1, len(imgs), i+1)
    plt.title(f'img{i+1}')
    plt.axis('off')
    plt.imshow(img[:, :, ::-1])

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
    hists.append(hist)

query = hists[0]
methods = {'CORREL': cv2.HISTCMP_CORREL, 'CHISQR': cv2.HISTCMP_CHISQR,
            'INTERSECT': cv2.HISTCMP_INTERSECT, 'BHATTACHARYYA': cv2.HISTCMP_BHATTACHARYYA}

for i, (name, method) in enumerate(methods.items()):
    print(f'{name:10s}', end='\t')
    for j, (hist, img) in enumerate(zip(hists, imgs)):
        ret = cv2.compareHist(query, hist, method)
        if method == cv2.HISTCMP_INTERSECT:
            ret = ret/np.sum(query)
        print(f'img{j+1}:{ret:9.2f}', end='\t')
    print()
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()