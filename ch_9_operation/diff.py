import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('./diff1.jpg')
img1 = img1[:500, :, :]
img2 = cv2.imread('./diff2.jpg')
img2 = img2[:500, :, :]

img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# diff = cv2.absdiff(img1, img2)
diff = cv2.absdiff(img1_gray, img2_gray)

_, diff = cv2.threshold(diff, 1, 255, cv2.THRESH_BINARY)
diff_cyan = cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)
diff_cyan[:, :, :2] = 0

spot = cv2.bitwise_xor(img2, diff_cyan)

imgs = {'img1': img1, 'img2': img2, 'diff': diff, 'spot': spot}
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 2, i+1)
    if i != 2:
        plt.imshow(v[:, :, ::-1])
    else:
        plt.imshow(v, 'gray')
    plt.title(k)
    plt.xticks([])
    plt.yticks([])
plt.show()