import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('./gradient.jpg', cv.IMREAD_GRAYSCALE)

_, t_bin = cv.threshold(image, 127, 255, cv.THRESH_BINARY)
_, t_bininv = cv.threshold(image, 127, 255, cv.THRESH_BINARY_INV)
_, t_trunc = cv.threshold(image, 127, 255, cv.THRESH_TRUNC)
_, t_2zr = cv.threshold(image, 127, 255, cv.THRESH_TOZERO)
_, t_2zrinv = cv.threshold(image, 127, 255, cv.THRESH_TOZERO_INV)

images = {'origin': image, 'binary': t_bin, 'binary_inv': t_bininv,
            'trunc': t_trunc, 'tozero': t_2zr, 'tozero_inv': t_2zrinv}

for i, (key, value) in enumerate(images.items()):
    plt.subplot(2, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([])
    plt.yticks([])
plt.show()