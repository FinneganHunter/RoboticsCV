import cv2 as cv
import numpy as np

# openCV/Data/haarcascades in downloads, openCV.zip
face_cascade = cv.CascadeClassifier('.../resources/haarcascade_frontalface_default.xml')
obj_cascade = cv.CascadeClassifier('')
# TODO: application: add in the different cascades for each recognizable object
# TODO: single module test: add in the different cascades for each recognizable object

# ComputerVision.computer_vision.video_feed() will be the parameter in app.py
# TODO: will this need to loop?

# TODO: add in the image recognition and tag processing module
# TODO: add the feed passing from this package to the video feed module


def video_feed(cam_num=0):
    """Begin video feed, any 'cap' is returned from here

    :type cam_num: int
    """
    capture = cv.VideoCapture(cam_num)  # parameter will vary based on the number of cameras on the system
    # capture = cv.VideoCapture('rtsp://username:password@192.168.1.64/1')
    return capture


def obj_recog(cap):

    ret, img = cap.read()
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)
    # below: generic placeholder for any number of objects to be recognized
    objs = obj_cascade.detectMultiScale(gray_img, 1.3, 5)

    # roi_finder(faces, 'faces', img, gray_img)
    # roi_finder(objs, 'faces', img, gray_img)

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roi_face_gray = gray_img[y:y + h, x:x + w]
        roi_face_color = img[y:y + h, x:x + w]

    for (x, y, w, h) in objs:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roi_obj_gray = gray_img[y:y + h, x:x + w]
        roi_obj_color = img[y:y + h, x:x + w]

    return roi_obj_gray, roi_obj_color


def roi_finder(recog, recog_name, img_param, gray_img_param):
    # TODO: ask gil how he got the concat in variable names to work
    print('idk')


def haarcascade_test(cap) -> tuple[any, any]:

    while True:

        ret, img = cap.read()
        gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)

        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            roi_gray = gray_img[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        # make it so they're just global variables that're changed
        # or concurrent.futures module
        print('rois:' + str(*roi_gray) + '\t' + str(*roi_color) + '\tin: ' + str(*img.shape))

        cv.imshow('feed', img)
        k = cv.waitKey(30) & 0xff
        if k == 27:
            break

        return roi_color, roi_gray

    cap.release()
    cv.destroyAllWindows()


def computer_vision_test():
    while True:
        cap = video_feed()

        ret, frame = cap.read()  # takes the
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('video feed', frame)
        cv.imshow('gray, gray')

        if cv.waitKey(1) & 0xFF == ord('q'):  #
            break

    cap.release()  #
    cv.destroyAllWindows()  #
