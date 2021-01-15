import cv2 as cv


def open_camera():
    capture = cv.VideoCapture(0)
    while(True):
        ret,frame = capture.read()
        cv.imshow("camera",frame)
        c = cv.waitKey(50)
        if c == 27:
            break


open_camera()