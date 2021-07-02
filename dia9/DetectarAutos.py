import cv2

cap = cv2.VideoCapture('imgs/video.avi')

if not cap.isOpened():
    raise IOError('No puede abrir la camara')

car_cascade = cv2.CascadeClassifier('imgs/cars.xml')

while True:
    ret,frame = cap.read()
    if not ret:
       break   

    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.1,1)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow('Camara',frame)
    c=cv2.waitKey(1)
    if c == 27:
        break

cv2.destroyAllWindows()