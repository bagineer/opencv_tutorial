import cv2 as cv
import numpy as np
import os.path as osp
from matplotlib import pyplot as plt

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'gradient.jpg'
img_file = osp.join(file_path, file_name)
image = cv.imread(img_file, cv.IMREAD_GRAYSCALE)

thresh = np.zeros_like(image)
thresh[image > 127] = 255

ret, thresh_cv = cv.threshold(image, 127, 255, cv.THRESH_BINARY)

images = {'Original': image, 'Numpy API': thresh, 'cv2.threshold': thresh_cv}
for i, (key, value) in enumerate(images.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([])
    plt.yticks([])

plt.show()