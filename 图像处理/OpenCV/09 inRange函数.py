import cv2 as cv
import numpy


def extrace_object_demo():
    capture = cv.VideoCapture("")   # 填入路径
    while(True):
        ret, frame = capture.read() # 读取视频的每一帧图片放进frame中
        if ret == False:    # ret是False表示视频读取完毕
            break;
        hsv = cv.cvtColor(frame, cv.COLOR_RGB2HSV) # 将每一帧变成HSV图片
        # 将要过滤出来的绿色的hsv三个值的最高值和最低值分别放入数组中
        lower_green_hsv = numpy.array([35, 43, 46])
        upper_green_hsv = numpy.array([77, 255, 255])
        # 返回二值化图像，其中绿色的物体全部变成白色，其他颜色全部变成黑色
        mask = cv.inRange(hsv, lower_green_hsv, upper_green_hsv)
        cv.imshow("track green", mask)   # 展示图片
        c = cv.waitKey(40)
        if c == 27:     # 27代表esc(escape)
            break;


