import cv2
import numpy as np
import matplotlib.pyplot as plt

#img = cv2.imread('imgs/gradiente.png',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('imgs/monedas1.jpg',cv2.IMREAD_GRAYSCALE)
ret, img1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret, img2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret, img3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret, img4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret, img5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titulos = ['Original','THRESH_BINARY','THRESH_BINARY_INV','THRESH_TRUNC','THRESH_TOZERO','THRESH_TOZERO_INV']
imgs = [img,img1,img2,img3,img4,img5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(imgs[i],cmap='gray')
    plt.title(titulos[i])
    plt.xticks([])
    plt.yticks([])
plt.waitforbuttonpress()
