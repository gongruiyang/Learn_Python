import cv2 as cv
import numpy
from matplotlib import pyplot


def plot_demo(image):
    pyplot.hist(image.ravel(), 256, [0, 256])
    pyplot.show()

def image_hist(image):
    color = ('blue', 'green', 'red')
    for i, color in  enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0,256])
        pyplot.plot(hist, color=color)
        pyplot.xlim([0, 256])
    pyplot.show()


def equalHist_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("equalHist_demo", dst)


def Clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow("Clahe_demo", dst)

image = cv.imread("01.jpg")
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
cv.imshow("image", image)
Clahe_demo(image)
cv.waitKey(0)
cv.destroyAllWindows()