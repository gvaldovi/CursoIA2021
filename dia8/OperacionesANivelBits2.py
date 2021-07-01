import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imgs/LogoCocaCola.png',cv2.COLOR_BGR2RGB)
imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
_,img_mask=cv2.threshold(imgGray,127,255,cv2.THRESH_BINARY)

imgResult = cv2.bitwise_not(img_mask)
imgResult2 = cv2.bitwise_and(img,img,mask=imgResult)

img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
imgResult2 = cv2.cvtColor(imgResult2,cv2.COLOR_RGB2BGR)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(img)
plt.subplot(142);plt.imshow(img_mask,cmap='gray')
plt.subplot(143);plt.imshow(imgResult,cmap='gray')
plt.subplot(144);plt.imshow(imgResult2)
plt.waitforbuttonpress()
