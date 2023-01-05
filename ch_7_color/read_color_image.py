import cv2 as cv

file_name = './sample.png'
image = cv.imread(file_name)
print(image.shape)
bgr = cv.imread(file_name, cv.IMREAD_COLOR)
bgra = cv.imread(file_name, cv.IMREAD_UNCHANGED)

cv.imshow('Color', image)
cv.imshow('BGR', bgr)
cv.imshow('B', bgra[:, :, 0])
cv.imshow('G', bgra[:, :, 1])
cv.imshow('R', bgra[:, :, 2])
cv.imshow('A', bgra[:, :, 3])
cv.waitKey(0)
cv.destroyAllWindows()