import cv2
import time

trackers = [cv2.TrackerBoosting_create,
            cv2.TrackerMIL_create,
            cv2.TrackerKCF_create,
            cv2.TrackerTLD_create,
            cv2.TrackerMedianFlow_create,
            cv2.TrackerGOTURN_create,
            cv2.TrackerCSRT_create,
            cv2.TrackerMOSSE_create]
tracker_idx = 0
tracker = None
is_first = True

cap = cv2.VideoCapture(0)
HEIGHT = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# FPS = 60
# DELAY = int(1000/FPS)

win_name = 'Tracking APIs'

while cap.isOpened():
    ret, frame = cap.read()
    st = time.time()
    if not ret:
        break

    img_draw = frame.copy()
    if tracker is None:
        cv2.putText(img_draw, 'Press the Spacebar to select ROI !!!', (20, 20),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2, cv2.LINE_AA)
    else:
        flag, bbox = tracker.update(frame)
        (x, y, w, h) = bbox
        if flag:
            cv2.rectangle(img_draw, (int(x), int(y)), (int(x + w), int(y + h)),
                          (0, 255, 0), 2, 1)
        else:
            cv2.putText(img_draw, 'Tracking failed ...', (20, 20),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2, cv2.LINE_AA)
    
    tracker_name = tracker.__class__.__name__
    cv2.putText(img_draw, f'{tracker_idx} : {tracker_name}', (100, 20),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(img_draw, f'FPS : {1/(time.time()-st):4.1f}', (20, HEIGHT-20),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow(win_name, img_draw)    

    key = cv2.waitKey(1) & 0xff
    if key == ord(' ') or is_first:
        is_first = False
        roi = cv2.selectROI(win_name, frame, False)
        
        if roi[2] and roi[3]:
            tracker = trackers[tracker_idx]()
            is_init = tracker.init(frame, roi)
    
    elif key in range(48, 56):
        tracker_idx = key - 48
        if bbox is not None:
            tracker = trackers[tracker_idx]()
            is_init = tracker.init(frame, roi)
        
    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()
