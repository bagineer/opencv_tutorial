import cv2 
import numpy as np
from matplotlib import pyplot as plt

def stack_images(imgs):
    global img_list
    img_dict = dict()
    for title, img in imgs:
        img_dict[title] = img
    img_list.append(img_dict)

img = cv2.imread('./grid.jpg')
img_list = []
stack_images([('Original', img)])

# Derivative
gx_k = np.array([[-1, 1]])
gy_k = np.array([[-1],
                 [1]])
edge_x = cv2.filter2D(img, -1, gx_k)
edge_y = cv2.filter2D(img, -1, gy_k)
stack_images([('Gradient x', edge_x), ('Gradient y', edge_y)])

# Roberts cross
gx_k = np.array([[1, 0],
                 [0, -1]])
gy_k = np.array([[0, 1],
                 [-1, 0]])
edge_x = cv2.filter2D(img, -1, gx_k)
edge_y = cv2.filter2D(img, -1, gy_k)
stack_images([('Roberts x', edge_x), ('Roberts y', edge_y)])

# Prewitt
gx_k = np.array([[-1, 0, 1],
                 [-1, 0, 1],
                 [-1, 0, 1]])
gx_k = np.array([[-1, -1, -1],
                 [0, 0, 0],
                 [1, 1, 1]])
edge_x = cv2.filter2D(img, -1, gx_k)
edge_y = cv2.filter2D(img, -1, gy_k)
stack_images([('Prewitt x', edge_x), ('Prewitt y', edge_y)])

# Sobel
gx_k = np.array([[-1, 0, 1],
                 [-2, 0, 2],
                 [-1, 0, 1]])
gx_k = np.array([[-1, -2, -1],
                 [0, 0, 0],
                 [1, 2, 1]])
edge_x = cv2.filter2D(img, -1, gx_k)
edge_y = cv2.filter2D(img, -1, gy_k)
stack_images([('Sobel x', edge_x), ('Sobel y', edge_y)])

# Scharr
gx_k = np.array([[-3, 0, 3],
                 [-10, 0, 10],
                 [-3, 0, 3]])
gx_k = np.array([[-3, -10, -3],
                 [0, 0, 0],
                 [3, 10, 3]])
edge_x = cv2.filter2D(img, -1, gx_k)
edge_y = cv2.filter2D(img, -1, gy_k)
stack_images([('Scharr x', edge_x), ('Scharr y', edge_y)])

for i, img_dict in enumerate(img_list):
    plt.figure(i)
    for j, (title, image) in enumerate(img_dict.items()):
        plt.subplot(1, 2, j+1)
        plt.title(title)
        plt.imshow(image)
        plt.axis('off')
plt.show()