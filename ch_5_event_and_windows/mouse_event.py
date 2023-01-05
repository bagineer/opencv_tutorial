import cv2
import os.path as osp

# Mouse Callback Function
def onMouse(event, x, y, flags, params):
    # print(event, flags)
    radius = 1
    color = (0, 0, 0)
    thickness = 1
    if event == cv2.EVENT_LBUTTONDOWN:
        # Click with ctrl + shift key
        if flags & cv2.EVENT_FLAG_CTRLKEY and flags & cv2.EVENT_FLAG_SHIFTKEY:
            thickness = 3
            radius = 10
            color = (255, 255, 0)
            
        # Click with ctrl key
        elif flags & cv2.EVENT_FLAG_CTRLKEY:
            thickness = 2
            radius = 15
            color = (0, 255, 0)

        # Click with shift key
        elif flags & cv2.EVENT_FLAG_SHIFTKEY:
            thickness = 1
            radius = 5
            color = (0, 0, 255)
        cv2.circle(img, (x, y), radius, color, thickness)
        cv2.imshow(title, img)


# Make window.
title = 'Mouse Event'
cv2.namedWindow(title)
cv2.setMouseCallback(title, onMouse)

# Read image.
img_path = '../ch_3_image_IO/captured'
img_file = 'captured_003.png'
img = cv2.imread(osp.join(img_path, img_file))

if img is not None:
    cv2.imshow(title, img)
    while True:
        if cv2.waitKey(0) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
else:
    print('No image')