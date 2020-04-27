import cv2 as cv

# openCV/Data/haarcascades in downloads, openCV.zip

# obj_cascade = cv.CascadeClassifier('')
# TODO: application: add in the different cascades for each recognizable object
# TODO: single module test: add in the different cascades for each recognizable object

# ComputerVision.computer_vision.video_feed() will be the parameter in app.py
# TODO: will this need to loop?

# TODO: add in the image recognition and tag processing module
# TODO: add the feed passing from this package to the video feed module

onerun_flag = False
face_data = {}


def video_feed(cam_num: int = 0):
    """Begin video feed, any 'cap' is returned from here

    :type cam_num: int
    """

    global onerun_flag
    print(f'video feed started with cam number: {cam_num}') if not onerun_flag else NULL
    onerun_flag = True

    capture = cv.VideoCapture(cam_num)  # parameter will vary based on the number of cameras on the system
    # capture = cv.VideoCapture('rtsp://username:password@192.168.1.64/1') # use if implementing IP camera

    return capture


# TODO: implement if multiple similar rois are within a few pixels of each other, an average is taken for a master roi
def obj_recog(cap):
    """runs object recognition any passed cascade"""

    # TODO: future proofing for different object cascades, cascade_name become passable
    cascade_name = 'haarcascade_frontalface_default.xml'
    roi_obj_color, roi_obj_gray = [0], [0]

    obj_cascade = cv.CascadeClassifier(f'.../resources/haar-cascade/{cascade_name}')

    ret, img = cap.read()
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    objs = obj_cascade.detectMultiScale(gray_img, 1.3, 5)
    # below: generic placeholder for any number of objects to be recognized
    # objs = obj_cascade.detectMultiScale(gray_img, 1.3, 5)

    # roi_finder(faces, 'faces', img, gray_img)
    # roi_finder(objs, 'faces', img, gray_img)

    # TODO: copy changes from face_reco about object tracking into obj_recog

    detected = 0 if not len(objs) else 1

    if detected:
        for (x, y, w, h) in objs:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # This is the actual pixels of the object within the video frame
            roi_obj_gray = gray_img[y:y + h, x:x + w]
            roi_obj_color = img[y:y + h, x:x + w]

    return roi_obj_color, roi_obj_gray


"""
def roi_finder(recog, recog_name, img_param, gray_img_param):
    # TODO: ask gil how he got the concat in variable names to work, might have to be a class
    # TODO: replaces the for loop for any given roi
    print('idk')
"""


def haarcascade_test(cap, escape_key='q'):  # works as intended, single cascade running
    """single cascade test, """

    global face_data
    face_cascade = cv.CascadeClassifier('../resources/haar-cascade/haarcascade_frontalface_default.xml')

    try:

        print(f'escape key is {escape_key}')

        while True:

            ret, img = cap.read()
            gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)

            for (x, y, w, h) in faces:
                cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                roi_gray = gray_img[y:y + h, x:x + w]
                roi_color = img[y:y + h, x:x + w]
                face_data = {'location': [x, y], 'size': [w, h]}

                # TODO: stores the location data for any number of simililar cascades, compares them all, finds ones ->
                # TODO: within a locational tolerance and averages them in that case
            # make it so they're just global variables that're changed -> done
            # or concurrent.futures module
            # print('rois:' + str(*roi_gray) + '\t' + str(*roi_color) + '\tin: ' + str(*img.shape))

            cv.imshow('haar_cascade feed', img)
            if cv.waitKey(1) & 0xFF == ord(escape_key):  #
                break

        cap.release()
        cv.destroyAllWindows()

    except EnvironmentError as e:
        print(str(e))


def computer_vision_test(cap, escape_key='q'):  # fully successful test of image processing
    try:

        print(f'escape key is {escape_key}')
        while True:

            ret, frame = cap.read()  # takes the
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            # cv.imshow('video feed', frame)
            cv.imshow('gray', gray)

            if cv.waitKey(1) & 0xFF == ord(escape_key):  #
                break

        cap.release()  #
        cv.destroyAllWindows()  #

    except EnvironmentError as e:
        print(str(e))
