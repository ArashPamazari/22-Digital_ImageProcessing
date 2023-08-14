import cv2
import numpy as np

orginal_image = cv2.imread('board - origin.bmp', 0)
test_image = cv2.imread('board - test.bmp', 0)
test = cv2.flip(test_image, 1)   # mirror kardan

result = cv2.subtract(test , orginal_image )
result = result * 100            #afzayesh contrast


cv2.imwrite('board.jpg', result)
