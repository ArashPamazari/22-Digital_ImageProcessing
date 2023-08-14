import cv2

image1 = cv2.imread('a.tif', 0)
image2 = cv2.imread('b.tif', 0)

result = cv2.subtract(image2, image1)

cv2.imwrite('sub.jpg', result)
