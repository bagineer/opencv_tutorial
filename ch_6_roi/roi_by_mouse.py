import cv2 as cv

def onMouse(event, x, y, flags, params):
    global x0, y0, is_dragging, roi
    if event == cv.EVENT_LBUTTONDOWN:
        print('left button down')
        is_dragging = True
        x0, y0 = x, y
    elif event == cv.EVENT_LBUTTONUP:
        if is_dragging:
            print('left button up')
            is_dragging = False
            copied = resized.copy()
            lx, ly, rx, ry = min(x, x0), min(y, y0), max(x, x0), max(y, y0)
            roi = resized[ly:ry, lx:rx]
            cv.rectangle(copied, (lx, ly), (rx, ry), (255, 0, 0), 2)
            cv.imshow(win_title, copied)
    elif event == cv.EVENT_MOUSEMOVE:
        if is_dragging:
            copied = resized.copy()
            lx, ly, rx, ry = min(x, x0), min(y, y0), max(x, x0), max(y, y0)
            cv.rectangle(copied, (lx, ly), (rx, ry), (0, 0, 255), 2)
            cv.imshow(win_title, copied)

orig_file = './sample.jpg'
orig_image = cv.imread(orig_file)
win_title = 'ROI by Mouse Click'
roi_idx = 1
x0, y0, is_dragging, roi = -1, -1, False, None
cv.namedWindow(win_title)
cv.setMouseCallback(win_title, onMouse)

if orig_image is not None:
    HEIGHT, WIDTH, _ = orig_image.shape
    SCALE = 0.2
    resized = cv.resize(orig_image, (int(WIDTH*SCALE), int(HEIGHT*SCALE)))
    cv.imshow(win_title, resized)

    while True:
        key = cv.waitKey(0)
        if key & 0xFF == 27:
            cv.imshow(win_title, resized)
        elif key == ord('q'):
            break
        elif key == ord('s'):
            cv.imwrite(f'./roi_{str(roi_idx).zfill(3)}.jpg', roi)
            cv.imshow('Selected ROI', roi)
            roi_idx += 1
    cv.destroyAllWindows()
else:
    exit(-1)