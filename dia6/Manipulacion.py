import cv2
import matplotlib.pyplot as plt

#img = cv2.imread('imgs/img_18x18.png',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('imgs/Barco.jpg',cv2.IMREAD_COLOR)

"""
img2 = img.copy()
img2[2,2] = 127
img2[2,3] = 127
img2[3,2] = 127
img2[3,3] = 127
"""
img2 = img[200:400,300:600]
#plt.imshow(img2)
#plt.waitforbuttonpress()
cv2.imshow('Imagen2',img2)
cv2.waitKey(0)

#img3 = cv2.resize(img2,None,fx=2,fy=2)
img3 = cv2.resize(img2,dsize=(100,200),interpolation=cv2.INTER_AREA)
cv2.imshow('Imagen3',img3)
cv2.waitKey(0)
#plt.imshow(img3)
#plt.waitforbuttonpress()

imgH=cv2.flip(img,1)
imgV=cv2.flip(img,0)
imgHV=cv2.flip(img,-1)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(imgH);plt.title('Horizontal');
plt.subplot(142);plt.imshow(imgV);plt.title('Vertical');
plt.subplot(143);plt.imshow(imgHV);plt.title('H-V');
plt.subplot(144);plt.imshow(img);plt.title('Original');
plt.waitforbuttonpress()

cv2.destroyAllWindows()