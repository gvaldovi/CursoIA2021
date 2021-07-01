import cv2

def deteccionContornosCanny(imagen):
    imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    imagen = cv2.Canny(imagen,30,80)
    return imagen

def deteccionContornosLaplace(imagen):
    imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    imagen = cv2.Laplacian(imagen,cv2.CV_64F)
    return imagen

def deteccionContornosSobely(imagen):
    imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    imagen = cv2.Sobel(imagen,cv2.CV_64F,dx=1,dy=0)
    return imagen

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError('No puede abrir la camara')

while True:
    ret,frame = cap.read()
    if not ret:
       break
        
    c=cv2.waitKey(1)
    if c == ord('a'):
        frame = deteccionContornosCanny(frame)
    if c == ord('s'):
        frame = deteccionContornosLaplace(frame)
    if c == ord('d'):
        frame = deteccionContornosSobely(frame)
            
    if c == 27:
        break
    cv2.imshow('Camara',frame)
cv2.release()
cv2.destroyAllWindows()
