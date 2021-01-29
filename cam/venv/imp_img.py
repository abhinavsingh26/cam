import cv2
print("Package Imported")

img = cv2.imread("C:/Users/ZERO/PycharmProjects/cam/lena.png")

cv2.imshow("Output", img)
cv2.waitKey(0)