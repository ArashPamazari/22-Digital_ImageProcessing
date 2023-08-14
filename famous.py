import cv2
import numpy as np

my_image = cv2.imread('me.jpg', 0)
john_image = cv2.imread('john.jpg', 0)

my_image = cv2.resize(my_image, (800, 800))
john_image = cv2.resize(john_image, (800, 800))
row , col  = my_image.shape

step2 = my_image//2 + john_image//4
step3 = my_image//4 + john_image//2

result = np.zeros((row, col*4), np.uint8)
result[0:row, 0:col] = my_image
result[0:row, col:col*2] = step2
result[0:row, col*2:col*3] = step3
result[0:row, col*3:col*4] = john_image

cv2.imwrite('famous.jpg', result)
