import cv2 as cv


def print_image_info(image):
    print(type(image))
    print(image.size)
    print(image.shape)
    print(image.dtype)


img = cv.imread("01.jpg")
print_image_info(img)