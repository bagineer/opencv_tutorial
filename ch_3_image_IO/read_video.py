import cv2
import os.path as osp

video_file = './recordings/video.avi'

cap = cv2.VideoCapture(video_file)
fps = 30.0

if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('Video', img)
            if cv2.waitKey(int(1000/fps)) != -1:  # int(1000/fps)
                break
        else:
            print('End of video.')
            break
    cap.release()
else:
    print('No video file.')
cv2.destroyAllWindows()