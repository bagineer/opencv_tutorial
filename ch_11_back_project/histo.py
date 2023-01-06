import cv2
from matplotlib import pyplot as plt

plt.style.use('classic')
img = cv2.imread('./sample.jpeg')

plt.subplot(211)
plt.imshow(img[:, :, ::-1])
plt.title('sample image')
plt.xticks([])
plt.yticks([])

hist = cv2.calcHist([img], [0,1], None, [32, 32], [0, 256, 0, 256])
plt.subplot(234)
p = plt.imshow(hist)
plt.title('Blue and Green')
plt.colorbar(p)

hist = cv2.calcHist([img], [1,2], None, [32, 32], [0, 256, 0, 256])
plt.subplot(235)
p = plt.imshow(hist)
plt.title('Green and Red')
plt.colorbar(p)

hist = cv2.calcHist([img], [0,2], None, [32, 32], [0, 256, 0, 256])
plt.subplot(236)
p = plt.imshow(hist)
plt.title('Blue and Red')
plt.colorbar(p)

plt.show()