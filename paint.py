import cv2

image = cv2.imread('Mona_Lisa.jpg', 0)

color = 255 - image
blurred = cv2.GaussianBlur(color, (21,21), 0)
image_blurred = 255 - blurred

sketch = image / image_blurred
sketch = sketch * 255

cv2.imwrite('paint.jpg', sketch)