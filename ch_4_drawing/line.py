import cv2
import os.path as osp
import random

img_path = '../ch_3_image_IO/captured'
img_file = 'captured_000.png'
img = cv2.imread(osp.join(img_path, img_file))
height, width, _ = img.shape
print(width, height)
x0, y0 = -1, -1
line_types = [cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA]

def onMouse(event, x, y, flags, params):
    global x0, y0, img, line_types
    
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    thickness = random.randint(1, 8)
    line_type = line_types[random.randint(0, 2)]



    # draw lines
    if event == cv2.EVENT_LBUTTONDOWN:
        if x0 > 0 and y0 > 0:
            print(x0, y0)
            cv2.line(img, (x0, y0), (x, y), (0, 255, 255), 4, cv2.LINE_AA)
            cv2.imshow('Drawing', img)
        x0, y0 = x, y

    # draw a rectangle
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     x0, y0 = x, y
    # elif event == cv2.EVENT_LBUTTONUP:
    #     print(f'rectangle / width : {abs(x - x0)}, height : {abs(y - y0)}, start : {(x0, y0)}, end : {(x, y)}')
    #     cv2.rectangle(img, (x0, y0), (x, y), color, thickness, line_type)
    #     cv2.imshow('Drawing', img)

if img is not None:
    cv2.line(img, (100, 200), (400, 400), (255, 255, 0), 1, cv2.LINE_4) # (x1, y1), (x2, y2)
    cv2.imshow('Drawing', img)
    cv2.setMouseCallback('Drawing', onMouse)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('No image file.')