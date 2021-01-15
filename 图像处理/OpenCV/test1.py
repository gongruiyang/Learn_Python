# 1.导入cv2模块
import cv2 as cv


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)


def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        cv.imshow("video", frame)
        cv.flip(frame, 1)
        c = cv.waitKey(50)
        if c == 27:
            break


# 2.使用imread()函数读入图片
src = cv.imread('01.jpg')
# 3.使用imshow()函数展示图片
cv.imshow("image", src)
# 4.使用waitKey()暂停程序
cv.waitKey(0)

# get_image_info(src)
# video_demo()
# 5.销毁创建窗口
cv.destroyAllWindows()
