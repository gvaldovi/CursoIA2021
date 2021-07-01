#Haar ,Viola Jones, HOG

import cv2

print(cv2.data.haarcascades)
face_xml = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_xml = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

def detectarRostro(gray,frame):
    rostros = face_xml.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in rostros:
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,0,0),2)
        roiGray = gray[y:y+h,x:x+w]
        roiColor = frame[y:y+h,x:x+w]
        ojos = eye_xml.detectMultiScale(roiGray)

        for (ox,oy,ow,oh) in ojos:
            cv2.rectangle(roiColor,(ox,oy),((ox+ow),(oy+oh)),(0,255,0),2)
    
    return frame

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError('No puede abrir la camara')

while True:
    ret,frame = cap.read()
    if not ret:
       break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = detectarRostro(gray,frame)

    cv2.imshow('Camara',frame)
    
    c=cv2.waitKey(1)
    if c == 27:
        break

cv2.release()
cv2.destroyAllWindows()

