import os.path as osp
import cv2

file_path = osp.dirname(osp.abspath(__file__))
img1 = cv2.imread(osp.join(file_path, 'sample1.jpg'))
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

img2 = cv2.imread(osp.join(file_path, 'sample2.jpg'))
img2 = cv2.resize(img2, (0, 0), None, 0.5, 0.5)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

## ORB
# matcher.match
orb = cv2.ORB_create()
kp_orb_1, desc_orb_1 = orb.detectAndCompute(gray1, None)
kp_orb_2, desc_orb_2 = orb.detectAndCompute(gray2, None)

matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
matches = matcher.match(desc_orb_1, desc_orb_2)

matches.sort(key = lambda x: x.distance)
min_dist, max_dist = matches[0].distance, matches[-1].distance

ratio = 0.2
nice_threshold = (max_dist - min_dist) * ratio + min_dist

nice_matches = [m for m in matches if m.distance < nice_threshold]
print(f'matches : {len(nice_matches)}, min : {min_dist}, max : {max_dist}, threshold : {nice_threshold}')

res = cv2.drawMatches(img1, kp_orb_1, img2, kp_orb_2, nice_matches, None,
                      flags = cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('ORB + matcher.match', res)

# matcher.knnMatch
matcher = cv2.BFMatcher(cv2.NORM_HAMMING2)
matches = matcher.knnMatch(desc_orb_1, desc_orb_2, 2)

ratio = 0.7
nice_matches = [f for f, s in matches if f.distance < s.distance * ratio]
print(f'matches : {len(nice_matches)}, {len(matches)}')

res = cv2.drawMatches(img1, kp_orb_1, img2, kp_orb_2, nice_matches, None,
                      flags = cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('ORB + KNN', res)



cv2.imshow('Template', img1)
cv2.imshow('Target', img2)
cv2.waitKey()
cv2.destroyAllWindows()