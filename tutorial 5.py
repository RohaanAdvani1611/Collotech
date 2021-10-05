import numpy as py
import cv2

car_cascade=cv2.CascadeClassifier('cars.xml')

img = cv2.imread('carimg.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cars = car_cascade.detectMultiScale(gray,1.1,3)


for (x,y,w,h) in cars:
    img = cv2.rectangle(img,(x,y),(x+w,y+h), (0,0,255),2)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()