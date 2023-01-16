import cv2
import os.path as osp

cap = cv2.VideoCapture(0)
file_path = osp.dirname(osp.abspath(__file__))
save_path = osp.join(file_path, 'captured')
save_name = 'captured'
save_idx = 0

if cap.isOpened():
    print("webcam is opened")

    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('Webcam', img)
            key = cv2.waitKey(1)
            if key == ord('q'):
                print('quit webcam.')
                break
            elif key == ord('s'):
                cv2.imwrite(f'{osp.join(save_path, save_name)}_{str(save_idx).zfill(3)}.png', img)
                save_idx += 1
        else:
            print('no frame.')
            break
else:
    print('webcam is not opened.')
cap.release()
cv2.destroyAllWindows()