import cv2 as cv

# Read image.
image_file = './sample.jpg'
image = cv.imread(image_file)

# Resize image.
HEIGHT, WIDTH, _ = image.shape
SCALE = 0.2
image = cv.resize(image, (int(WIDTH*SCALE), int(HEIGHT*SCALE)))

if image is not None:
    cv.imshow('Select ROI', image)

    while True:
        x, y, w, h = cv.selectROI('image', image)
        if w and h:
            roi = image[y:y+h, x:x+w]
            cv.imshow('ROI', roi)

        if cv.waitKey(0) == ord('q'):
            cv.destroyAllWindows()
            break
else:
    exit(-1)
