import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imgs/Musica.png',cv2.IMREAD_GRAYSCALE)
ret, img1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
img2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
img3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

titulos = ['Original','UMBRAL GLOBAL','ADAPTIVE_THRESH_MEAN_C','ADAPTIVE_THRESH_GAUSSIAN_C']
imgs = [img,img1,img2,img3]

for i in range(len(imgs)):
    plt.subplot(2,2,i+1),plt.imshow(imgs[i],cmap='gray')
    plt.title(titulos[i])
    plt.xticks([])
    plt.yticks([])
plt.waitforbuttonpress()