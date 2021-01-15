import cv2 as cv


def func(image):
    cv.imshow("image", image)
    image_ = cv.bitwise_not(image)
    cv.imshow("image_", image_)
image = cv.imread("01.jpg")
func(image)
cv.waitKey(0)
cv.destroyAllWindows()