import cv2
import os.path as osp
import random

## Settings
file_path = '../ch_3_image_IO/captured'
file_name = 'captured_000.png'
img_file = osp.join(file_path, file_name)
img_orig = cv2.imread(img_file)
img_gray = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
win_gray = 'img_gray Window'
win_orig = 'Origin Window'

win_empty = 'Empty Window'
x, y = 200, 200


if img_orig is not None and img_gray is not None:
    cv2.namedWindow(win_gray)
    cv2.imshow(win_gray, img_gray)

    cv2.namedWindow(win_empty)

    cv2.namedWindow(win_orig, cv2.WINDOW_NORMAL)
    cv2.imshow(win_orig, img_orig)

    cv2.moveWindow(win_gray, 100, 100)
    cv2.moveWindow(win_orig, 300, 300)
    cv2.moveWindow(win_empty, x, y)

    while True:
        wait_key = cv2.waitKey(1)
        # Quit.
        if wait_key == ord('q'):
            break
        # Resize empty window.
        elif wait_key == ord('r'):
            cv2.resizeWindow(win_empty, random.randint(300, 600), random.randint(300, 600))
        # Move empty window.
        elif wait_key == ord('m'):
            x, y = random.randint(0, 400), random.randint(0, 400)
            cv2.moveWindow(win_empty, x, y)
        # Destroy gray window.
        elif wait_key == ord('1'):
            cv2.destroyWindow(win_gray)
        # Destroy origin window.
        elif wait_key == ord('3'):
            cv2.destroyWindow(win_orig)
        # Move empty window to upside.
        elif wait_key == ord('w'):
            y -= 5
            cv2.moveWindow(win_empty, x, y)
        # Move empty window to downside.
        elif wait_key == ord('s'):
            y += 5
            cv2.moveWindow(win_empty, x, y)
        # Move empty window to leftside.
        elif wait_key == ord('a'):
            x -= 5
            cv2.moveWindow(win_empty, x, y)
        # Move empty window to rightside.
        elif wait_key == ord('d'):
            x += 5
            cv2.moveWindow(win_empty, x, y)

    cv2.destroyAllWindows()
else:
    print('No image file.')