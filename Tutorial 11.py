import cv2
import numpy as np
img = cv2.imread("sudoku.png")
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
_, th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
img = cv2.imshow("original", img)
img = cv2.imshow("th1", th1)
img = cv2.imshow("th2", th2)
img = cv2.imshow("th3", th3)
cv2.waitKey(0)
cv2.destroyAllWindows()