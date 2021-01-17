import cv2 as cv
import numpy


def blur_demo(image):
    dst = cv.blur(image, (20, 1))
    cv.imshow("dst", dst)

def mid_blur(image):
    dst = cv.medianBlur(image, 5)
    cv.imshow("dst", dst)

def cus_blur(image):
    # kernel = numpy.ones([17, 17], numpy.float32) / 200
    kernel = numpy.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], numpy.float32)
    dst = cv.filter2D(image, -1, kernel=kernel)
    cv.imshow("dst", dst)



image = cv.imread("01.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", image)
cus_blur(image)
cv.waitKey(0)
cv.destroyAllWindows()