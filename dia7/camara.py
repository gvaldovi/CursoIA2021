import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError('No puede abrir la camara')

while True:
    ret,frame = cap.read()
    if not ret:
       break

    frame=cv2.flip(frame,1)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

    cv2.imshow('Camara',frame)
    c=cv2.waitKey(1)
    if c == 27:
        break

cv2.release()
cv2.destroyAllWindows()
