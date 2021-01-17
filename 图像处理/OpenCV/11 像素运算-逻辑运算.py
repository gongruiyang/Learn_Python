import cv2 as cv
import numpy


def logic_demo(image1, image2):
    dst = cv.bitwise_and(image1, image2)
    cv.imshow("and", dst)
    dst = cv.bitwise_not(image1, image2)
    cv.imshow("not", dst)
    dst = cv.bitwise_or(image1, image2)
    cv.imshow("or", dst)
    dst = cv.bitwise_xor(image1, image2)
    cv.imshow("xor", dst)


def contract_brightness_demo(image, c, b):
    h, w, ch = image.shape
    blank = numpy.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow("change", dst)

# src1 = cv.imread("star.jpg")
# src2 = cv.imread("hourse.jpg")
# src1 = cv.resize(src1, (300, 400))
# src2 = cv.resize(src2, (300, 400))
# dst = cv.addWeighted(src1, 1, src2, 1, 5)
# cv.imshow("src1", src1)
# cv.imshow("src2", src2)
# cv.imshow("dst", dst)
image = cv.resize(cv.imread("01.jpg"), (300, 400))
cv.imshow("image",image)
contract_brightness_demo(image, 1.2, 10)
cv.waitKey(0)
cv.destroyAllWindows()