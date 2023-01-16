import cv2
import os
import os.path as osp

## Settings
# Read image.
file_path = osp.dirname(osp.abspath(__file__))
file_path = osp.abspath(osp.join(file_path, os.pardir, 'ch_3_image_IO/captured'))
file_name = 'captured_002.png'
img_file = osp.join(file_path, file_name)
img = cv2.imread(img_file)

cx, cy, x1, y1 = -1, -1, -1, -1
lx, ly, sx, sy = -1, -1, -1, -1
is_dragging, button_idx = False, -1
title = 'Circle and Ellipse'
lidx, ridx = 0, 0

# Mouse Callback Function
def onMouse(event, x, y, flags, params):
    global img, cx, cy, x1, y1, is_dragging, button_idx, lidx, ridx

    # Put text into middle of the circle.
    def put_text(img, cx, cy, text, fontFace, fontScale, thickness):
        (tw, th), _ = cv2.getTextSize(text, fontFace, fontScale, thickness)   # text width, text height
        print(tw, th)
        cv2.rectangle(img, (cx-tw//2, cy-th//2), (cx+tw//2, cy+th//2), (255, 255, 255), -1)
        cv2.putText(img, text, (cx-tw//2, cy+th//2), fontFace, fontScale, (0, 0, 0), thickness)

    # left button event
    # Draw a circle with a center point and radius.
    if event == cv2.EVENT_LBUTTONDOWN:
        is_dragging, button_idx = True, 0
        cx, cy = x, y
        lidx += 1
    elif event == cv2.EVENT_MOUSEMOVE:
        if is_dragging and button_idx == 0:
            coppied_img = img.copy()
            hw, hh = abs(x-cx), abs(y-cy)   # half width, half height
            cv2.circle(coppied_img, (cx, cy), int((hw*hw + hh*hh)**0.5), (255, 0, 255))
            cv2.imshow(title, coppied_img)
            cv2.waitKey(1)
    elif event == cv2.EVENT_LBUTTONUP:
        if is_dragging and button_idx == 0:
            hw, hh = abs(x-cx), abs(y-cy)   # half width, half height
            cv2.circle(img, (cx, cy), int((hw*hw + hh*hh)**0.5), (0, 0, 255), 2)
            # cv2.putText(img, f'left_{lidx}', (cx, cy), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
            put_text(img, cx, cy, f'left_{lidx}', cv2.FONT_HERSHEY_PLAIN, 1, 1)
            cv2.imshow(title, img)
            is_dragging = False

    # right button event
    # Draw a circle with two points and diameter.
    if event == cv2.EVENT_RBUTTONDOWN:
        is_dragging, button_idx = True, 2
        x1, y1 = x, y
        ridx += 1
        print(x1, y1)
    elif event == cv2.EVENT_MOUSEMOVE:
        if is_dragging and button_idx == 2:
            coppied_img = img.copy()
            w, h = x-x1, y-y1
            cx, cy = x1 + int(w//2), y1 + int(h//2)
            cv2.circle(coppied_img, (cx, cy), int((w*w + h*h)**0.5 // 2),  (255, 255, 0))
            cv2.imshow(title, coppied_img)
            cv2.waitKey(1)
    elif event == cv2.EVENT_RBUTTONUP:
        if is_dragging and button_idx == 2:
            w, h = x-x1, y-y1
            cx, cy = x1 + int(w//2), y1 + int(h//2)
            cv2.circle(img, (cx, cy), int((w*w + h*h)**0.5 // 2),  (255, 0, 0), -1)
            put_text(img, cx, cy, f'right_{ridx}', cv2.FONT_HERSHEY_PLAIN, 1, 1)
            cv2.imshow(title, img)
            is_dragging = False
        

if img is not None:
    # draw ellipses
    cv2.ellipse(img, (100, 100), (50, 30), 0, 0, 360, (0, 0, 255), 2)
    cv2.ellipse(img, (100, 100), (30, 50), 0, 0, 360, (0, 255, 255), 2)
    cv2.ellipse(img, (300, 300), (100, 50), 30, 180, 360, (255, 0, 0), 2)
    cv2.ellipse(img, (300, 300), (100, 50), 150, 180, 0, (0, 255, 255), 2)
    cv2.circle(img, (300, 300), 75, (0, 0, 255), -1)
    cv2.ellipse(img, (300, 300), (100, 50), 30, 180, 0, (255, 0, 0), 2)
    cv2.ellipse(img, (300, 300), (100, 50), 150, 180, 360, (0, 255, 255), 2)

    cv2.imshow(title, img)
    cv2.setMouseCallback(title, onMouse)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('No iamge.')