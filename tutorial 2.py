import cv2
img = cv2.imread('messi15.png')
import numpy as np
def click_event(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		font = cv2.FONT_HERSHEY_PLAIN
		strXY= str(x) + ',' + str(y)
		cv2.putText(img,strXY,(x,y),font,0.5,(255,0,0),1)
		cv2.imshow('image',img)

cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
