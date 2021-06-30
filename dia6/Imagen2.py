import cv2
import matplotlib.pyplot as plt

#8 bits sin signo (00000000 - 11111111) 2^8=256 (0-255), uint8

#Modelos Color:RGB
#img = cv2.imread('imgs/img_18x18.png',cv2.IMREAD_GRAYSCALE)
#img = cv2.imread('imgs/img1.png',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('imgs/img1.png')

#RGB
#BGR

#print(img)
print(img.shape)
#imgRGB = img[:,:,::-1]
#imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#HSV (Hue, Saturation, Value)
#r,g,b=cv2.split(imgRGB)
h,s,v=cv2.split(imgHSV)
nuevo_h=h+10
r=nuevo_h
g=s
b=v

img2 = cv2.merge((r,g,b))
img3 = cv2.cvtColor(img2,cv2.COLOR_HSV2RGB)

plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(r, cmap='gray');plt.title('Canal Rojo');
plt.subplot(142);plt.imshow(g, cmap='gray');plt.title('Canal Verde');
plt.subplot(143);plt.imshow(b, cmap='gray');plt.title('Canal Azul');

plt.subplot(144);plt.imshow(img3);plt.title('Imagen Unida');
cv2.imwrite('img_copy.png',img3)

#plt.imshow(imgInv)
#plt.imshow(img,cmap='gray')
plt.waitforbuttonpress()
#cv2.imshow('Imagen',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()