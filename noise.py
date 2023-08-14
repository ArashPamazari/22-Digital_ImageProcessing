import numpy as np
import random

import cv2

image = cv2.imread('chess pieces.jpg', 0)

row, col = image.shape

for i in range(row):
    for j in range(col):
        noise = random.randint(0, row)
        if noise % (row//3)  == 0:
            if image[i, j] < 170:
                image[i, j] = 255
            else:
                image[i, j] = 0


cv2.imwrite('noise.jpg', image)
