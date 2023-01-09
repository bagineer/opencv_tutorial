import cv2
import numpy as np

win_name = 'Liquify'
half = 50
is_dragging = False

def triangle_affine_transform(roi, pts1, pts2, w, h):
    m = cv2.getAffineTransform(np.float32(pts1), np.float32(pts2))
    warped = cv2.warpAffine(roi.copy(), m, (w, h), None,
                            cv2.INTER_LINEAR, cv2.BORDER_REFLECT_101)
    mask = np.zeros((h, w), dtype=np.uint8)
    cv2.fillConvexPoly(mask, np.int32(pts2), (255, 255, 255))
    
    warped = cv2.bitwise_and(warped, warped, mask=mask)
    
    return warped, mask

def liquify(img, cx1, cy1, cx2, cy2):
    x, y, w, h = cx1 - half, cy1 - half, 2*half, 2*half
    roi = img[y:y+h, x:x+w].copy()
    out = roi.copy()

    offset_cx1, offset_cy1 = cx1 - x, cy1 - y
    offset_cx2, offset_cy2 = cx2 - x, cy2 - y

    tri1 = [[(0, 0), (w, 0), (offset_cx1, offset_cy1)],
            [(0, 0), (0, h), (offset_cx1, offset_cy1)],
            [(w, 0), (w, h), (offset_cx1, offset_cy1)],
            [(0, h), (w, h), (offset_cx1, offset_cy1)]]
    tri2 = [[(0, 0), (w, 0), (offset_cx2, offset_cy2)],
            [(0, 0), (0, h), (offset_cx2, offset_cy2)],
            [(w, 0), (w, h), (offset_cx2, offset_cy2)],
            [(0, h), (w, h), (offset_cx2, offset_cy2)]]
    
    for pts1, pts2 in zip(tri1, tri2):
        warped, mask = triangle_affine_transform(roi, pts1, pts2, w, h)
        out = cv2.bitwise_and(out, out, mask=cv2.bitwise_not(mask))
        out += warped

    img[y:y+h, x:x+w] = out
    return img
    
def onMouse(event, x, y, flags, param):
    global cx1, cy1, is_dragging, img

    if event == cv2.EVENT_LBUTTONDOWN:
        is_dragging = True
        cx1, cy1 = x, y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        img_draw = img.copy()
        cv2.rectangle(img_draw, (x-half, y-half), (x+half, y+half), (0, 0, 255))
        cv2.imshow(win_name, img_draw)

    elif event == cv2.EVENT_LBUTTONUP:
        if is_dragging:
            is_dragging = False
            liquify(img, cx1, cy1, x, y)
            cv2.imshow(win_name, img)

img = cv2.imread('./sample.jpg')
h, w, _ = img.shape

cv2.namedWindow(win_name)
cv2.setMouseCallback(win_name, onMouse)
cv2.imshow(win_name, img)

while True:
    key = cv2.waitKey(1)
    if key & 0xFF == 27:
        break
cv2.destroyAllWindows()