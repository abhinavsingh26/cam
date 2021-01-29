import cv2
import numpy as np

img = cv2.imread("C:/Users/ZERO/PycharmProjects/cam/lena.png")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
imgBlur = cv2.GaussianBlur(imgGray, (11, 11), 0)
imgCanny = cv2.Canny(img, 150, 100)
imgDialation = cv2.dilate(imgCanny, kernel , iterations= 1  )
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDialation)

cv2.waitKey(0)