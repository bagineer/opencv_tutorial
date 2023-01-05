import cv2
import os
import os.path as osp

cap = cv2.VideoCapture(0)

if cap.isOpened():
    file_path = './recordings/'

    if not osp.exists(file_path):
        os.mkdir(file_path)

    # Settings
    video_file = 'video.avi'
    img_file = 'recording'
    img_idx = 0
    fps = 10.0
    codec = 'DIVX' # ['D', 'I', 'V', 'X']
    # fourcc = cv2.VideoWriter_fourcc(*codec)
    # fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
    fourcc = cv2.VideoWriter_fourcc(*codec)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height))
    outWriter = cv2.VideoWriter(file_path + video_file, fourcc, fps, size)

    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('Video capture', img)
            outWriter.write(img)
            waitKey = cv2.waitKey(int(1000/fps))
            # Quit.
            if waitKey == ord('q'):
                break
            # Save as an image.
            elif waitKey == ord('s'):
                cv2.imwrite(f'{file_path + img_file}_{str(img_idx).zfill(3)}.png', img)
                img_idx += 1
        else:
            print('no frame')
            break
    outWriter.release()
else:
    print('No webcam.')
cap.release()
cv2.destroyAllWindows()