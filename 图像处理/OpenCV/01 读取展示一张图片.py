import cv2 as cv

img = cv.imread("01.jpg")
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()