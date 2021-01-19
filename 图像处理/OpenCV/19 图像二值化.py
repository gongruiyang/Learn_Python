import cv2 as cv
import numpy


def threshold_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
    print("threshold value %s" % ret)
    cv.imshow("Binary IMage", binary)


def local_threshold_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("Binary IMage", binary)


image = cv.resize(cv.imread("01.jpg"), (300,400))
cv.imshow("image", image)
local_threshold_demo(image)
cv.waitKey(0)
cv.destroyAllWindows()