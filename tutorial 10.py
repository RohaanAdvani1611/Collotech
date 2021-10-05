import cv2
import numpy as np
img = cv2.imread("gradient.png")
#In binary threshold, pixels of intensity less than 127 will appear black and those after will appear white
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#Binary threshold inverse is the opposite of Binary threshold
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# in Trunc threshold, pixels of intensity less than 127 remain as they were and those more than 127 remain at 127
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
#Image is black till 127 and unchanged after 127
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
#Tozero Threshold inverse is the opposite of Tozero Threshold
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
img = cv2.imshow("original", img)
img = cv2.imshow("th1", th1)
img = cv2.imshow("th2", th2)
img = cv2.imshow("th3", th3)
img = cv2.imshow("th4", th4)
img = cv2.imshow("th5", th5)
cv2.waitKey(0)
cv2.destroyAllWindows()
