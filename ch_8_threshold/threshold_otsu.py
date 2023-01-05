import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('./Lenna.png', cv.IMREAD_GRAYSCALE)
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