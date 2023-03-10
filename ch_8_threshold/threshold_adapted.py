import cv2 as cv
import os.path as osp
from matplotlib import pyplot as plt

block_size = 7
C = 5
file_path = osp.dirname(osp.abspath(__file__))
file_name = 'Lenna.png'
img_file = osp.join(file_path, file_name)
image = cv.imread(img_file, cv.IMREAD_GRAYSCALE)

t, t_otsu = cv.threshold(image, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
t_mean = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, block_size, C)
t_gauss = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, block_size, C)

images = {'images': image, f't_otsu:{t:.0f}': t_otsu, 'adaptive_mean': t_mean, 'adaptive_gauss':t_gauss}

for i, (key, value) in enumerate(images.items()):
    plt.subplot(2, 2, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([])
    plt.yticks([])
plt.show()