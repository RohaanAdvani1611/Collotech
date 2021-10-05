import cv2
import numpy as np
img = cv2.imread("messi15.png")
cv2.imshow("img1",img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread("template1.png",0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
th=0.9;
loc=np.where(res>=th)
print(loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0,255,0), 3)
cv2.imshow("img2",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
