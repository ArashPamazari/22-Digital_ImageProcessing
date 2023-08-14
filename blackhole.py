import cv2
import numpy as np

imagelist = [[0 for i in range(5)]for j in range(4)]   #save image in 2D list 5 col and 4 row
for i in range(4):
    for j in range(5):
        imagelist[i][j] = cv2.imread(f'black hole/{i+1}/{j+1}.jpg', 0)
        row, col = imagelist[i][j].shape  # save image size 

image2 = [0 for i in range(4)]
for i in range(4):
    for j in range(5):
        image2[i] += imagelist[i][j]//5

result = np.zeros((row*2 , col*2), dtype= np.uint8)

# location of images:

result[0:row, 0:col] = image2[0]
result[0:row, col:col*2] = image2[1]
result[row:row*2, 0:col] = image2[2]
result[row:row*2, col:col*2] = image2[3]


cv2.imwrite('blackhole.jpg', result)

