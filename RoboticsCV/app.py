# open cv module
# arduino communication module
# remote control?
# wifi camera stream
from typing import List, Any

from .ArduinoComm.class_test import ArduinoCommClass
from RoboticsCV.ComputerVision import computer_vision, face_recog
import cv2 as cv


def main():
    """
    # 1: Run the camera (module or script) WifiCam
    # 2: Start the computer vision (module) starts openCV & returns the roi
    # 3: Start Arduino communication (module) takes the roi & verifies communication
    # 4: Run computer vision in different modes: image, object, face recognition / tracking (function in a module)
    # 5: Make movements / operations based on assigned/defined task (functions in a module)
    """

    print('this ran')

    # 1
    # some script to start IP camera stream
    # video feed is VideoCapture
    # set_wh is global variables for dimensions of the video
    video = computer_vision.video_feed()
    face_recog.set_wh(video)

    # 2
    arduino = ArduinoCommClass(5, 6, 13, 19)
    print(*arduino.pin_nums)

    # 3
    # ArduinoCommClass.comm_verify(7)

    while True:
        # 4
        # computer_vision.computer_vision_test(video) # test works perfectly well
        # computer_vision.obj_recog(video)        # loop over or run as process/thread

        # TODO: execute video capture in it's own thread
        # video capture up to: ret, img = cap.read() -> gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # TODO: execute in it's own thread
        # Based on runtime, lag, and continuous operation, there's just going to have to be a master recog
        # function/module that gets called for all the models and cascades that want to be run
        # maybe it should just take a list of string with cascade names and adds them to teh list of ones that should be
        # run in either their own threaded or processes.

        #TODO
        # Might be able to make it so only 1 view of any object or face, if 1 dectected: lock into just using that one;
        # if not detected: parse to see if another perspective works: frontal -> 3/4 -> profile

        # should probably also find out a way to combine the rois and coordinates being output

        face_recog.single_face(video)                      # necessary for individual frame processing
        # face_recog.multi_face_loop(video)  # wont work until reject
        # ier is implemented

        # loop over face_recog or computer_vision,  class variables get updated for speed & turning
        app_face_data = face_recog.face_data
        app_img_data = face_recog.width, face_recog.height
        print(f'face data {app_face_data} in image {app_img_data}')

        arduino.positional_data(app_face_data, app_img_data)

        # computer_vision.haarcascade_test(video) # necessary to test haar cascade recognition
        # TODO: this would never be hit, define a loop which would take the data
        # capture thread and processing thread

        if cv.waitKey(1) & 0xFF == 27:
            break

        # 5
        # arduino.turning()             # loop over turning
        # arduino.movement()               # loop over speed

    video.release()
    cv.destroyAllWindows()

# test parallelism vs serial for end of program optimization
