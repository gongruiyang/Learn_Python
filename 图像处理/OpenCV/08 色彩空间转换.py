import cv2 as cv

def color_space_change(image):
    RGB2YUV_img = cv.cvtColor(image, cv.COLOR_RGB2YUV)
    cv.imshow("RGB2YUV_img", RGB2YUV_img)
    YUV2RGB_img = cv.cvtColor(RGB2YUV_img, cv.COLOR_YUV2RGB)
    cv.imshow("YUV2RGB_img", YUV2RGB_img)


img = cv.imread("01.jpg")
color_space_change(img)
cv.waitKey(0)
cv.destroyAllWindows()
