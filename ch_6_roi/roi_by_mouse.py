import cv2
import os.path as osp

def onMouse(event, x, y, flags, params):
    global x0, y0, is_dragging, roi
    if event == cv2.EVENT_LBUTTONDOWN:
        print('left button down')
        is_dragging = True
        x0, y0 = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        if is_dragging:
            print('left button up')
            is_dragging = False
            copied = resized.copy()
            lx, ly, rx, ry = min(x, x0), min(y, y0), max(x, x0), max(y, y0)
            roi = resized[ly:ry, lx:rx]
            cv2.rectangle(copied, (lx, ly), (rx, ry), (255, 0, 0), 2)
            cv2.imshow(win_title, copied)
    elif event == cv2.EVENT_MOUSEMOVE:
        if is_dragging:
            copied = resized.copy()
            lx, ly, rx, ry = min(x, x0), min(y, y0), max(x, x0), max(y, y0)
            cv2.rectangle(copied, (lx, ly), (rx, ry), (0, 0, 255), 2)
            cv2.imshow(win_title, copied)

file_path = osp.dirname(osp.abspath(__file__))
file_name = 'sample.jpg'
img_file = osp.join(file_path, file_name)
orig_image = cv2.imread(img_file)
win_title = 'ROI by Mouse Click'
roi_idx = 1
x0, y0, is_dragging, roi = -1, -1, False, None
cv2.namedWindow(win_title)
cv2.setMouseCallback(win_title, onMouse)

if orig_image is not None:
    HEIGHT, WIDTH, _ = orig_image.shape
    SCALE = 0.2
    resized = cv2.resize(orig_image, (int(WIDTH*SCALE), int(HEIGHT*SCALE)))
    cv2.imshow(win_title, resized)

    while True:
        key = cv2.waitKey(0)
        if key & 0xFF == 27:
            cv2.imshow(win_title, resized)
        elif key == ord('q'):
            break
        elif key == ord('s'):
            cv2.imwrite(osp.join(file_path, f'roi_{str(roi_idx).zfill(3)}.jpg'), roi)
            cv2.imshow('Selected ROI', roi)
            roi_idx += 1
    cv2.destroyAllWindows()
else:
    exit(-1)