import cv2 as cv
import numpy


image = cv.imread("01.jpg")
B, G, R = cv.split(image)
cv.namedWindow("image", cv.WINDOW_NORMAL)
cv.imshow("image", image)
# cv.imshow("R", R)
# cv.imshow("G", G)
# cv.imshow("B", B)
change_image = cv.merge([B, G, R])
cv.imshow("change_image", change_image)
cv.waitKey(0)
cv.destroyAllWindows()