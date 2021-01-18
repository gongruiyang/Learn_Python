import cv2 as cv
import numpy
from matplotlib import pyplot


def hist2d_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image], [0, 1], None, [100, 250], [0, 100, 0, 256])
    # cv.imshow("hist2D", hist)
    pyplot.imshow(hist, interpolation='nearest')
    pyplot.title("2D Histogram")
    pyplot.show()


def back_projection_demo():
    target = cv.imread("01.jpg")
    sample = cv.imread("sample.jpg")
    sam_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    tar_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    # 展示图片
    cv.imshow("target", target)
    cv.imshow("sample", sample)

    sam_hist = cv.calcHist([sam_hsv], [0, 1], None, [36, 48], [0, 100, 0, 256])
    cv.normalize(sam_hsv, sam_hsv, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([tar_hsv], [0, 1], sam_hist, [0, 100, 0, 256], 1)
    cv.imshow("BackProjectionDemo", dst)

# image = cv.imread("01.jpg")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", image)
# hist2d_demo(image)
back_projection_demo()
cv.waitKey(0)
cv.destroyAllWindows()