#Haar ,Viola Jones, HOG

import cv2, os


face_xml = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

datasets = 'datasets'
subFolder = 'valdovinos'

path = os.path.join(datasets,subFolder)
if not os.path.isdir(path):
    os.makedirs(path)

def detectarRostro(gray,frame):
    rostros = face_xml.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in rostros:
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(255,0,0),2)
        face = gray[y:y+h,x:x+w]
        face2 = cv2.resize(face,(50,30))
        cv2.imwrite('%s/%s.png' % (path,cont), face2)
    
    return frame

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError('No puede abrir la camara')

cont = 1
#while True:
while cont <= 30:
    ret,frame = cap.read()
    if not ret:
       break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = detectarRostro(gray,frame)

    cv2.imshow('Camara',frame)
    
    cont += 1

    c=cv2.waitKey(1)
    if c == 27:
        break

cv2.release()
cv2.destroyAllWindows()

