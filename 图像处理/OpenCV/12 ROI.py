import cv2 as cv
import numpy

image = cv.resize(cv.imread("star.jpg"), (400, 300))
cv.imshow("image", image)
# 选取出目标区域
region = image[50:200, 100:250]
# 将目标区域变成灰色
gray = cv.cvtColor(region, cv.COLOR_BGR2GRAY)
# 再将目标区域放回原图
image[50:200, 100:250] = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow("image", image)
cv.waitKey(0)
cv.destroyAllWindows()