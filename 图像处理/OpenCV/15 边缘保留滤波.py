import cv2 as cv
import numpy


# def demo(image):
#     dst = cv.bilateralFilter(image, 0, 100, 15)
#     cv.imshow("dst",dst)


def demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.imshow("dst",dst)



image = cv.imread("01.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", image)
demo(image)
cv.waitKey(0)
cv.destroyAllWindows()