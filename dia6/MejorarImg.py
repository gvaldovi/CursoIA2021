import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imgs/Costa.jpg',cv2.IMREAD_COLOR)
imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(imgRGB.shape)

#m=np.ones(imgRGB.shape,dtype='uint8')*50
m=np.ones(imgRGB.shape)*0.8
m2=np.ones(imgRGB.shape)*1.2


#img1 = cv2.add(img,m)
#img2 = cv2.subtract(img,m)

img1 = np.uint8(cv2.multiply(np.float64(img),m))
img2 = np.uint8(np.clip(cv2.multiply(np.float64(img),m2),0,255))

#plt.figure(figsize=[18,5])
#plt.subplot(131);plt.imshow(img2);plt.title('Oscura');
#plt.subplot(132);plt.imshow(img);plt.title('Original');
#plt.subplot(133);plt.imshow(img1);plt.title('Clara');

plt.figure(figsize=[18,5])
plt.subplot(131);plt.imshow(img1);plt.title('Bajo constraste');
plt.subplot(132);plt.imshow(img);plt.title('Original');
plt.subplot(133);plt.imshow(img2);plt.title('Alto constraste');

#Segmentar una imagen: Extraer Regiones de Interés
#Umbral

#cv2.threshold()

#plt.imshow(imgRGB)
plt.waitforbuttonpress()