import cv2 as cv
import numpy


def flood_fill_demo(image):
    copy_image = image.copy()   # 拷贝图片
    h, w = image.shape[:2]    # 获取图片宽和高
    mask = numpy.zeros([h + 2, w + 2], numpy.uint8)  # 获取一张mask，其大小必须比原图长和宽大2
    cv.imshow("mask", mask)
    cv.floodFill(copy_image, mask, (380, 30), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("flood_fill_image", copy_image)


def fill_binary_demo():
    # 创建一张中间白周围黑的图片
    image = numpy.zeros([400, 400, 3], numpy.uint8)
    image[100:300, 100:300, :] = 255
    cv.imshow("image", image)

    # 创建遮罩图
    mask = numpy.ones([402, 402, 1], numpy.uint8)
    mask[101:301, 101:301] = 0
    # 从（200,200）点向周围填充(0, 0, 255)这个颜色
    cv.floodFill(image, mask, (200, 200), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("filled image", image)



# image = cv.resize(cv.imread("star.jpg"), (400, 300))
# cv.imshow("image", image)
fill_binary_demo()
cv.waitKey(0)
cv.destroyAllWindows()