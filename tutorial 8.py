import numpy as np
import cv2
def nothing(x):
    pass
cv2.namedWindow("image")
img = np.zeros((300,512,3),np.unit8)

cv2.createTrackbar('B', "image", 0, 255, nothing())
cv2.createTrackbar('G', "image", 0, 255, nothing())
cv2.createTrackbar('R', "image", 0, 255, nothing())

while (1):
    cv2.imshow("image",img)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
    b = cv2.getTrackbarPos('B', "image")
    g = cv2.getTrackbarPos('B', "image")
    r = cv2.getTrackbarPos('B', "image")

    img[:]=[b,g,r]
cv2.destroyAllWindows()