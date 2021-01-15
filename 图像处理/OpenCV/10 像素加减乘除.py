import cv2 as cv
import numpy


def add_demo(image1, image2):
    final_image = cv.add(image1, image2)
    cv.imshow("add", final_image)


def subtract_demo(image1, image2):
    final_image = cv.subtract(image1, image2)
    cv.imshow("subtract", final_image)


def divide_demo(image1, image2):
    final_image = cv.divide(image1, image2)
    cv.imshow("divide", final_image)


def multiply_demo(image1, image2):
    final_image = cv.multiply(image1, image2)
    cv.imshow("multiply", final_image)

image1 = cv.imread("01.jpg")
add_demo(image1, image1)
subtract_demo(image1, image1)
divide_demo(image1, image1)
multiply_demo(image1, image1)
cv.waitKey(0)
cv.destroyAllWindows()