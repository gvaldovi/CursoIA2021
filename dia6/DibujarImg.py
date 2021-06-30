import cv2
import matplotlib.pyplot as plt

img = cv2.imread('imgs/Apollo11.jpg',cv2.IMREAD_COLOR)
imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

cv2.line(imgRGB,(200,100),(400,100),(255,255,0),thickness=5,lineType=cv2.LINE_AA)
cv2.circle(imgRGB,(900,500),100,(255,0,0),thickness=5,lineType=cv2.LINE_AA)

cv2.rectangle(imgRGB,(500,100),(700,600),(255,0,255),thickness=5,lineType=cv2.LINE_8)

cv2.putText(imgRGB,'Este es Apollo 11',(200,600),cv2.FONT_HERSHEY_PLAIN,2.5,(0,0,255),thickness=2,lineType=cv2.LINE_AA)

plt.imshow(imgRGB)
plt.waitforbuttonpress()