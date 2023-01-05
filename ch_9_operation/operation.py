import cv2
import numpy as np

a = np.uint8([[200, 50]])
b = np.uint8([[100, 100]])

# print(a.shape, b.shape)

add_1 = a + b
sub_1 = a - b
mult_1 = a * 2.23123
div_1 = a / 7

print('Numpy Operations')
print(f'add : {add_1}, sub : {sub_1}, mult : {mult_1}, div : {div_1}')

add_2 = cv2.add(a, b)
sub_2 = cv2.subtract(a, b)
mult_2 = cv2.multiply(a, 2.23123)
div_2 = cv2.divide(a, 7)

print('openCV Operations')
print(f'add : {add_2}, sub : {sub_2}, mult : {mult_2}, div : {div_2}')