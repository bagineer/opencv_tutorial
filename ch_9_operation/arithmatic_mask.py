import cv2
import numpy as np

a = np.uint8([[1, 2]])
b = np.uint8([[10, 20]])
mask = np.uint8([[1, 0]])

c1 = cv2.add(a, b, None, mask)      # c1 = a + b
print(c1, b)
c2 = cv2.add(a, b, b.copy(), mask)  # c2 = b + (a + b)
print(c2, b)
c3 = cv2.add(a, b, b, mask)         # c3 = b + (a + b) = b
print(c3, b)
