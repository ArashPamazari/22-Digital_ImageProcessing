import cv2

image1=cv2.imread("images\ssss.jpg",0)
image2=cv2.imread("images\ttt.jpg",0) # zero means gray scale

# baray jam kardan 2 tasvir bayad baham ham andaze bashand.

#print(image1.shape)
#print(image2.shape) # baraye inke abAd tasavir ro bebinim chejorie

result = image1+image2

cv2.imshow('output',result)
cv2.waitKey()


# baraye inke jam 2 ta pixel az 255 bishtar nashe aval tasavir ro taqsim bar 2 mikonim

result = image1 // 2 +image2 // 2

cv2.imshow('output',result)
cv2.waitKey()



# code kahesh noise :

image1=cv2.imread("images\G1.jpg",0)
image2=cv2.imread("images\G2.jpg",0)
image3=cv2.imread("images\G3.jpg",0)
image4=cv2.imread("images\G4.jpg",0)
image5=cv2.imread("images\G5.jpg",0)
image6=cv2.imread("images\G6.jpg",0)


result = image1 // 6 + image2 // 6 + image3 // 6 + image4 // 6 + image5 // 6 + image6 // 6 

cv2.imshow('output',result)
cv2.waitKey()

# better code use loops
import cv2
import numpy as np


images = []
for i in range(1,7):
    image = cv2.imread(f'images/galaxy/g{i}.jpg',0)
    images.append(image)
    rows , cols = image.shape

result = np.zeros((rows,cols) , dtype="unit8") # yek araye ie baram besaz ke hame khonehash zero e ba andaze 1730*1428 va typesh int bashe
for image in images:
    result+=image//6

cv2.imshow('output',result)
cv2.waitKey()


# tafrigh 2ta tasvir :

import cv2
import numpy as np

image1= cv2.imread('images/d1.jpg',0)
image2= cv2.imread('images/d2.jpg',0)

result= image1 - image2


cv2.imshow('output',result)
cv2.waitKey()

# baraye inke meghdar pixelha manfi nashe :
# tasvir pezeshki

import cv2
import numpy as np

image1= cv2.imread('images/a.tif',0)
image2= cv2.imread('images/b.tif',0)

result= cv2.subtract(image1 , image2 ) # tabe baraye jologiri az on moshkel


cv2.imshow('output',result)
cv2.waitKey()


# zarb tasavir :
# mask * dandun
import cv2
import numpy as np

image1= cv2.imread('images/c.tif',0)
mask= cv2.imread('images/d.tif',0)


#result = image1 * image2

mask = mask // 255 #taqsim ke pixelhaye roshan ke 255 hastan beshan 1 ta tasvir dar ghesmat mask tire nashe

result= image1 * mask  


cv2.imshow('output',result)
cv2.waitKey()




# taqsim tasavir : 
# noorpardazi yeknavakht roye tasvir

import cv2
import numpy as np

image1= cv2.imread('images/e.tif',0)
image2 = cv2.imread('images/f.tif',0)
# baraye inke be moshkel taqsim bar sefr nashim mask nabayad 0 ya tire bashe
result = image1 / image2

cv2.imshow('output',result) # inja doroste vali toie imwrite siahe
cv2.waitKey() 

result = result * 255 # toie imwrite doroste 
cv2.imwrite('output.jpg',result)






