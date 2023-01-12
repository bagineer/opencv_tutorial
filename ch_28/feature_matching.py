import cv2
import numpy as np
import os

file_path = os.path.dirname(os.path.abspath(__file__))

img1 = cv2.imread(os.path.join(file_path, 'sample1.jpg'))
img1 = cv2.resize(img1, (0, 0), None, 0.7, 0.7, cv2.INTER_LINEAR)
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

img2 = cv2.imread(os.path.join(file_path, 'sample2.jpg'))
img2 = cv2.resize(img2, (0, 0), None, 0.7, 0.7, cv2.INTER_LINEAR)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('Template', img1)
cv2.imshow('Target', img2)

# BFMatcher + SIFT
detector = cv2.xfeatures2d.SIFT_create()
kp1, desc1 = detector.detectAndCompute(gray1, None)
kp2, desc2 = detector.detectAndCompute(gray2, None)

matcher = cv2.BFMatcher(cv2.NORM_L1, crossCheck = True)
matches = matcher.match(desc1, desc2)
res = cv2.drawMatches(img1, kp1, img2, kp2, matches, None,
                      flags = cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('BFMatcher + SIFT', res)

# BFMatcher + SURF
detector = cv2.xfeatures2d.SURF_create()
kp1, desc1 = detector.detectAndCompute(gray1, None)
kp2, desc2 = detector.detectAndCompute(gray2, None)

matcher = cv2.BFMatcher(cv2.NORM_L2, crossCheck = True)
matches = matcher.match(desc1, desc2)
res = cv2.drawMatches(img1, kp1, img2, kp2, matches, None,
                      flags = cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('BFMatcher + SURF', res)

cv2.waitKey()
cv2.destroyAllWindows()