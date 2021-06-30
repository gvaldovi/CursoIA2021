import cv2

#Modelos Color:RGB
img = cv2.imread('imgs/img1.png')
print(img.shape)
print(img.ndim)
print(img.shape[0])

img[:,:,0]=0
#img[:,:,1]=0
img[:,:,2]=0

cv2.imshow('Imagen Robot',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


