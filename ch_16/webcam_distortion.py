import cv2
import numpy as np

cap = cv2.VideoCapture(0)
WIDTH, HEIGHT = 480, 360
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
h, w = HEIGHT, WIDTH
mapy, mapx = np.indices((h, w), dtype=np.float32)

# Horizontal reflection
map_mirrorh_x, map_mirrorh_y = mapx.copy(), mapy.copy()
map_mirrorh_x[:, w//2:] = w - map_mirrorh_x[:, w//2:] - 1

# Vertical reflection
map_mirrorv_x, map_mirrorv_y = mapx.copy(), mapy.copy()
map_mirrorv_y[h//2:, :] = h - map_mirrorv_y[h//2:, :] - 1

# Wave
map_wave_x, map_wave_y = mapx.copy(), mapy.copy()
map_wave_x = map_wave_x + 15 * np.sin(mapy / 20)
map_wave_y = map_wave_y + 15 * np.sin(mapx / 20)

# Lens
map_lens_x, map_lens_y = 2*mapx/(w-1) - 1, 2*mapy/(h-1) - 1
r, theta = cv2.cartToPolar(map_lens_x, map_lens_y)
SCALE, EXP_CONVEX, EXP_CONCAVE = 1, 2, 0.5

# Convex
r_convex = r.copy()
r_convex[r < SCALE] = r_convex[r < SCALE]**EXP_CONVEX
map_convex_x, map_convex_y = cv2.polarToCart(r_convex, theta)
map_convex_x = ((map_convex_x + 1)*w - 1) / 2
map_convex_y = ((map_convex_y + 1)*h - 1) / 2

# Concave
r_concave = r.copy()
r_concave[r < SCALE] = r_concave[r < SCALE]**EXP_CONCAVE
map_concave_x, map_concave_y = cv2.polarToCart(r_concave, theta)
map_concave_x = ((map_concave_x + 1)*w - 1) / 2
map_concave_y = ((map_concave_y + 1)*h - 1) / 2

while True:
    ret, frame = cap.read()
    frame = frame[:HEIGHT, :WIDTH]

    mirrorh = cv2.remap(frame, map_mirrorh_x, map_mirrorh_y, cv2.INTER_LINEAR)
    mirrorv = cv2.remap(frame, map_mirrorv_x, map_mirrorv_y, cv2.INTER_LINEAR)
    wave = cv2.remap(frame, map_wave_x, map_wave_y, cv2.INTER_LINEAR,
                     None, cv2.BORDER_REPLICATE)
    convex = cv2.remap(frame, map_convex_x, map_convex_y, cv2.INTER_LINEAR)
    concave = cv2.remap(frame, map_concave_x, map_concave_y, cv2.INTER_LINEAR)

    r1 = np.hstack((frame, mirrorh, mirrorv))
    r2 = np.hstack((wave, convex, concave))
    merged = np.vstack((r1, r2))

    cv2.imshow('Mirror Dimension', merged)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
