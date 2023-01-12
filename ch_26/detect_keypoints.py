import cv2
import numpy as np

# Harris Corner Detection
img = cv2.imread('./sample.jpg')
img_draw = img.copy()
img_gray = cv2.cvtColor(img_draw, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', img)

corner = cv2.cornerHarris(img_gray, 2, 7, 0.2)
coords = np.where(corner > 0.1 * corner.max())
coords = np.stack((coords[1], coords[0]), axis = -1)

for i, (x, y) in enumerate(coords):
    cv2.circle(img_draw, (x, y), 5, (min(i, 255), 255 - min(i, 255), 0), 1, cv2.LINE_AA)

corner_norm = cv2.normalize(corner, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
corner_norm = cv2.cvtColor(corner_norm, cv2.COLOR_GRAY2BGR)

cv2.imshow('Harris', img_draw)

# Shi-Tomasi Detection
img_draw = img.copy()
corners = cv2.goodFeaturesToTrack(img_gray, 30, 0.01, 10)
corners = np.int32(corners)

for i, corner in enumerate(corners):
    x, y = corner[0]
    cv2.circle(img_draw, (x, y), 3, (min(i, 255), 0, 255 - min(i, 255)), 1, cv2.LINE_AA)

cv2.imshow('GFTT Shi - Tomasi', img_draw)

# GFTTDetection (Good Features To Track)
img_draw = img.copy()

gftt = cv2.GFTTDetector_create()
keypoints = gftt.detect(img_gray, None)

img_draw = cv2.drawKeypoints(img_draw, keypoints, None)
cv2.imshow('GFTT', img_draw)

# FAST (Feature from Accelerated Segment Test)
img_draw = img.copy()

fast = cv2.FastFeatureDetector_create(100)
keypoints = fast.detect(img_gray, None)
img_draw = cv2.drawKeypoints(img_draw, keypoints, None)

cv2.imshow('FAST', img_draw)

# SimpleBlobDetector
img_draw = img.copy()

detector = cv2.SimpleBlobDetector_create()
keypoints = detector.detect(img_gray)
img_draw = cv2.drawKeypoints(img_draw, keypoints, None, (0, 0, 255),
                             flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('SBD', img_draw)

# SimpleBlobDetector with filter options
img_draw = img.copy()

params = cv2.SimpleBlobDetector_Params()
params.minThreshold = 10
params.maxThreshold = 240
params.thresholdStep = 5

params.filterByArea = True
params.minArea = 300

params.filterByColor = False
params.filterByConvexity = False
params.filterByInertia = False
params.filterByCircularity = False

detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(img_gray)
img_draw = cv2.drawKeypoints(img_draw, keypoints, None, None,
                             flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('SBD with filter options', img_draw)

cv2.waitKey()
cv2.destroyAllWindows()