import cv2
import numpy as np
img = cv2.imread("shapes.PNG")
gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(gr, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    app = cv2.approxPolyDP(contour, (0.01*cv2.arcLength), (contour,True), True)
    cv2.drawContours(img, [app], 0, (0,255,0), 1)
    x=app.revel()[0]
    y=app.revel()[1]
    if len(app)==3:
        cv2.putText(img, "Triangle", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1)
    elif len(app)==4:
        x1, y1, w, h = cv2.boundingRect(app)
        aspectRatio = float(w)/h
        if aspectRatio>=0.95 and aspectRatio<=1.05:
            cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
        else:
            cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
    elif len(app)==5:
        cv2.putText(img, "Pentagon", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1)
    elif len(app)==10:
        cv2.putText(img, "Star", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1)
    else :
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
cv2.imshow("Shapes",img)
cv2.waitKey(0)
cv2.destroyAllwindows()
