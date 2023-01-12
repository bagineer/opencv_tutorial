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

## BFM
# BFMatcher + SIFT
sift = cv2.xfeatures2d.SIFT_create()
kp_sift_1, desc_sift_1 = sift.detectAndCompute(gray1, None)
kp_sift_2, desc_sift_2 = sift.detectAndCompute(gray2, None)

matcher = cv2.BFMatcher(cv2.NORM_L1, crossCheck = True)
matches = matcher.match(desc_sift_1, desc_sift_2)
res = cv2.drawMatches(img1, kp_sift_1, img2, kp_sift_2, matches, None,
                      flags = cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('BFMatcher + SIFT', res)

# BFMatcher + SURF
surf = cv2.xfeatures2d.SURF_create()
kp_surf_1, desc_surf_1 = surf.detectAndCompute(gray1, None)
kp_surf_2, desc_surf_2 = surf.detectAndCompute(gray2, None)

matcher = cv2.BFMatcher(cv2.NORM_L2, crossCheck = True)
matches = matcher.match(desc_surf_1, desc_surf_2)
res = cv2.drawMatches(img1, kp_surf_1, img2, kp_surf_2, matches, None,
                      flags = cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('BFMatcher + SURF', res)

# BFMatcher + ORB
orb = cv2.ORB_create()
kp_orb_1, desc_orb_1 = orb.detectAndCompute(gray1, None)
kp_orb_2, desc_orb_2 = orb.detectAndCompute(gray2, None)

matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
matches = matcher.match(desc_orb_1, desc_orb_2)
res = cv2.drawMatches(img1, kp_orb_1, img2, kp_orb_2, matches, None,
                      flags = cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('BFMatcher + ORB', res)

## FLANN
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

# FLANN + SIFT
matcher = cv2.FlannBasedMatcher(index_params, search_params)
matches = matcher.match(desc_sift_1, desc_sift_2)
res = cv2.drawMatches(img1, kp_sift_1, img2, kp_sift_2, matches, None,
                      flags = cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('FLANN + SIFT', res)

# FLANN + SURF
matcher = cv2.FlannBasedMatcher(index_params, search_params)
matches = matcher.match(desc_surf_1, desc_surf_2)
res = cv2.drawMatches(img1, kp_surf_1, img2, kp_surf_2, matches, None,
                      flags = cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('FLANN + SURF', res)

# FLANN + ORB
FLANN_INDEX_LSH = 6
index_params = dict(algorithm = FLANN_INDEX_LSH,
                    table_number = 6,
                    key_size = 12,
                    multi_probe_level = 1)
search_params = dict(checks = 30)

matcher = cv2.FlannBasedMatcher(index_params, search_params)
matches = matcher.match(desc_orb_1, desc_orb_2)
res = cv2.drawMatches(img1, kp_orb_1, img2, kp_orb_2, matches, None,
                      flags = cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('FLANN + ORB', res)

cv2.waitKey()
cv2.destroyAllWindows()