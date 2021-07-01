import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError('No puede abrir la camara')

while True:
    ret,frame = cap.read()
    if not ret:
       break
    
    h,w = frame.shape[:2]
    #3/2,3//2,3%2
    centro = (w//2,h//2)
    matrizGiro = cv2.getRotationMatrix2D(centro,-45,1.0)
    frame = cv2.warpAffine(frame,matrizGiro,(w,h))

    cv2.imshow('Camara',frame)
    c=cv2.waitKey(1)
    if c == 27:
        break

cv2.release()
cv2.destroyAllWindows()
