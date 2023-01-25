import cv2
import glob
import os
import os.path as osp


def img2hash(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.resize(img_gray, (16, 16))
    mean = img_gray.mean()
    binary = 1 * (img_gray > mean)
    return binary

def hamming_distance(a, b):
    a = a.reshape(1, -1)
    b = b.reshape(1, -1)
    dist = (a != b).sum()
    return dist


file_path = osp.dirname(osp.abspath(__file__))
file_name = 'pistol.jpg'
img_file = osp.join(file_path, file_name)
img = cv2.imread(img_file)

# Hasing
binary = img2hash(img)

dhash = []
for row in binary.tolist():
    s = ''.join([str(i) for i in row])
    dhash.append('%02x'%(int(s,2)))
dhash = ''.join(dhash)
cv2.putText(img, dhash, (10, 20), cv2.FONT_HERSHEY_PLAIN,
            0.6, (0, 0, 255), 1)

# Hash Matching
query = img2hash(img)
HAMMING_DIST_THRESHOLD = 0.25

search_dir = osp.join(file_path, os.pardir, '101_ObjectCategories')
img_path = glob.glob(search_dir + '/**/*.jpg')

for path in img_path:
    searching = cv2.imread(path)
    cv2.imshow('Searching ...', searching)
    cv2.waitKey(5)

    searching_hash = img2hash(searching)
    dist = hamming_distance(query, searching_hash)

    if dist / 256 < HAMMING_DIST_THRESHOLD:
        print(path, dist / 256)
        cv2.imshow(path, searching)

cv2.imshow('Image', img)
cv2.waitKey()
cv2.destroyAllWindows()