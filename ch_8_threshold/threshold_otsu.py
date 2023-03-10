import cv2 as cv
import os.path as osp
from matplotlib import pyplot as plt

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'Lenna.png'
img_file = osp.join(file_path, file_name)
image = cv.imread(img_file, cv.IMREAD_GRAYSCALE)
_, t_140 = cv.threshold(image, 140, 255, cv.THRESH_BINARY)
t, t_otsu = cv.threshold(image, -1, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
print('Otsu threshold :', t)

images = {'original': image, 't:140': t_140, f'otsu:{t:.0f}':t_otsu}

for i, (key, value) in enumerate(images.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([])
    plt.yticks([])
plt.show()