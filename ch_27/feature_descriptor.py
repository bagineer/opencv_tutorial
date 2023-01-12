import cv2
import numpy as np

img = cv2.imread('./sample.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# SIFT
sift = cv2.xfeatures2d.SIFT_create()
keypoints, descriptor = sift.detectAndCompute(img_gray, None)
print(f'keypoints : {len(keypoints)}, descriptor : {descriptor.shape}')

img_draw = cv2.drawKeypoints(img, keypoints, None,
                             flags = cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
cv2.imshow('SIFT', img_draw)

# SURF
surf = cv2.xfeatures2d.SURF_create(1000, 3, True, True)
keypoints, descriptor = surf.detectAndCompute(img_gray, None)
print(f'keypoints : {len(keypoints)}, descriptor : {descriptor.shape}')

img_draw = cv2.drawKeypoints(img, keypoints, None,
                             flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SURF', img_draw)

# ORB
orb = cv2.ORB_create()
keypoints, descriptor = orb.detectAndCompute(img_gray, None)
print(f'keypoints : {len(keypoints)}, descriptor : {descriptor.shape}')

img_draw = cv2.drawKeypoints(img, keypoints, None,
                             flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('ORB', img_draw)

cv2.waitKey()
cv2.destroyAllWindows()