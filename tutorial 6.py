import numpy as np
import cv2

img = cv2.imread("mulcar.jpg")
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, 0)
contours , _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    (x,y,w,h) = cv2.boundingRect(contour)

    if cv2.contourArea(contour)<700:
        continue
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

#cv2.drawContours(img, contours, -1, (0,255,0), 1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
