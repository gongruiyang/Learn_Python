import cv2 as cv
import numpy


def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    return pv

def gaussion_noise(image):
    h, w, c = image.shape
    for row in range(w):
        for col in range(h):
            s = numpy.random.normal(0, 20, 3)
            B = image[row, col, 0]
            G = image[row, col, 1]
            R = image[row, col, 2]
            image[row, col, 0] = clamp(B + s[0])
            image[row, col, 1] = clamp(G + s[1])
            image[row, col, 2] = clamp(R + s[2])
    cv.imshow("noise image", image)

image = cv.imread("01.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", image)
gaussion_noise(image)
cv.waitKey(0)
cv.destroyAllWindows()