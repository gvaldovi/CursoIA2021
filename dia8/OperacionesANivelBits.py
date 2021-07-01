import cv2
import numpy as np
import matplotlib.pyplot as plt

imgRect = cv2.imread('imgs/rectangulo.jpg',cv2.IMREAD_GRAYSCALE)
imgCir = cv2.imread('imgs/circulo.jpg',cv2.IMREAD_GRAYSCALE)

#1&1=1 , otro caso 0
#imgResult = cv2.bitwise_and(imgRect,imgCir,mask=None)
#imgResult = cv2.bitwise_or(imgRect,imgCir,mask=None)
imgResult = cv2.bitwise_xor(imgRect,imgCir,mask=None)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(imgRect,cmap='gray')
plt.subplot(142);plt.imshow(imgCir,cmap='gray')
plt.subplot(143);plt.imshow(imgResult,cmap='gray')
print(imgRect.shape)

plt.waitforbuttonpress()
