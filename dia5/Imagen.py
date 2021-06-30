import cv2
import matplotlib.pyplot as plt

#8 bits sin signo (00000000 - 11111111) 2^8=256 (0-255), uint8

#Modelos Color:RGB
#img = cv2.imread('imgs/img_18x18.png',cv2.IMREAD_GRAYSCALE)
#img = cv2.imread('imgs/img1.png',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('imgs/img1.png')

#RGB
#BGR

print(img)
print(img.shape)
imgInv = img[:,:,::-1]
r,g,b=cv2.split(imgInv)
plt.imshow(r)

#plt.imshow(imgInv)
#plt.imshow(img,cmap='gray')
plt.waitforbuttonpress()
#cv2.imshow('Imagen',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


