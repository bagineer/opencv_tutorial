import cv2
from matplotlib import pyplot as plt

'''
# Gray Scale
img = cv2.imread('./Lenna.png', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.subplot(2, 1, 1)
plt.imshow(img, 'gray')
plt.title('image')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 1, 2)
plt.plot(hist)
plt.show()
'''

# Color
img = cv2.imread('./Lenna.png')
plt.subplot(1, 2, 1)
plt.imshow(img[:, :, ::-1])
plt.title('image')
plt.xticks([])
plt.yticks([])

colors = ['b', 'g', 'r']
for i, color in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.subplot(1, 2, 2)
    plt.plot(hist, color=color)
plt.show()

