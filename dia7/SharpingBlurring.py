import cv2
import numpy as np

img = cv2.imread('imgs/carro.jpg')
cv2.imshow('Imgen Original',img)
cv2.waitKey()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagen Gray',imgGray)
cv2.waitKey()

#filtro = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
filtro = np.ones((3,3))

imgSharped = cv2.filter2D(imgGray,-1,kernel=filtro)

cv2.imshow('Imagen Sharped',imgSharped)
cv2.waitKey()

cv2.destroyAllWindows()
