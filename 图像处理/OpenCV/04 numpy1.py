import numpy as np
import cv2 as cv


def access_pexels(image):
    # print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    # print("宽度：%d,高度：%d,通道：%d" % (width, height, channels))
    for row in range(width):
        for col in range(height):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv;
    # cv.imshow("image", image)

def create_image():
    # img = np.zeros([300,300,3], np.uint8)   # 创建一个400*400的3通道的图片，dtype为np.uint8
    # cv.imshow("img", img)
    # img[:, :, 0] = np.ones([300, 300]) * 255
    # cv.imshow("img_", img)
    img = np.zeros([300,300,1], np.uint8)
    cv.imshow("img", img)
    img[:, :, 0] = np.ones([300, 300]) * 127
    cv.imshow("img_", img)

# img = cv.imread("01.jpg")
# cv.imshow("image_", img)
# t1 = cv.getTickCount();
# access_pexels(img)
# t2 = cv.getTickCount();
# running_time = 1000 * (t2 - t1) / cv.getTickFrequency()
# print('running time: %s (ms)' % running_time)
create_image()
cv.waitKey(0)
cv.destroyAllWindows();
