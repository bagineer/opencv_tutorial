import cv2
import os.path as osp
from matplotlib import pyplot as plt

plt.style.use('classic')
file_path = osp.dirname(osp.abspath(__file__))
file_name = 'sample.jpeg'
img_file = osp.join(file_path, file_name)
img = cv2.imread(img_file)

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