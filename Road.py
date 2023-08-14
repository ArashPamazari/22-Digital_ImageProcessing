import cv2
import numpy as np

images = []
for i in range(15):
    input = cv2.imread(f'highway/h{i}.jpg', 0)
    images.append(input)
    row, col = input.shape

results = np.zeros((row, col), np.uint8)
for image in images:
    results += image // 15

cv2.imwrite('Road.jpg', results)

