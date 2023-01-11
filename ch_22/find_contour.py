import cv2
import numpy as np

# img = cv2.imread('./sample.png')
# h, w, _ = img.shape
# img = cv2.resize(img, (w//2, h//2), interpolation=cv2.INTER_LINEAR)
# coppied1 = img.copy()

# img_gray = img[:, :, 0]
# ret, img_binary = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)


img = np.ones((200, 600, 3), np.uint8)*255

# draw polygons
cv2.rectangle(img, (20, 20), (180, 180), (0, 0, 0), -1)
cv2.fillPoly(img, [np.array([[300, 20], [210, 180], [390, 180]])], (0, 0, 0))
cv2.circle(img, (500, 100), 80, (0, 0, 0), -1)

# draw holes
cv2.rectangle(img, (40, 40), (160, 160), (255, 255, 255), -1)
cv2.fillPoly(img, [np.array([[300, 50], [240, 160], [360, 160]])], (255, 255, 255))
cv2.circle(img, (500, 100), 70, (255, 255, 255), -1)

img_gray = img[:, :, 0]
_, img_binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
coppied1 = img.copy()
coppied2 = img.copy()
coppied3 = img.copy()

# 1. Contour External and Approximate None
_, contour, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contour, -1, (255, 0, 0), 8)
for c in contour:
    for p in c:
        cv2.circle(img, tuple(p[0]), 2, (0, 0, 255), -1)
cv2.putText(img, f'CHAIN_APPROX_NONE, Number of contours : {len(contour)}',
            (0, 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)

# 2. Contour External and Approximate Simple
_, contour2, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(coppied1, contour2, -1, (255, 0, 0), 8)
for c in contour2:
    for p in c:
        cv2.circle(coppied1, tuple(p[0]), 2, (0, 0, 255), -1)
cv2.putText(coppied1, f'CHAIN_APPROX_SIMPLE, Number of contours : {len(contour2)}',
            (0, 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)

# 3. Contour Tree and Approximate Simple
_, contour3, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)
print(hierarchy)

for i, c in enumerate(contour3):
    color = np.random.randint(0, 255, 3).tolist()
    cv2.drawContours(coppied2, contour3, i, color, 8)
    cv2.putText(coppied2, str(i), tuple(c[0][0]), cv2.FONT_HERSHEY_PLAIN,
                1.5, (0, 0, 255), 2)
cv2.putText(coppied2, f'TREE HiERARCHY & CHAIN_APPROX_SIMPLE, Number of contours : {len(contour2)}',
            (0, 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)


merged = np.vstack((img, coppied1, coppied2))

cv2.imshow('Contour', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()