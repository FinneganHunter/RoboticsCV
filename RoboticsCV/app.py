# open cv module
# arduino communication module
# remote control?
# wifi camera stream

from .ArduinoComm.class_test import ArduinoCommClass, comm_verify
from RoboticsCV.ComputerVision import computer_vision


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
    cap = computer_vision.video_feed()

    # 2
    arduino = ArduinoCommClass(5, 6, 13, 19)
    print(*arduino.pin_nums)

    # 4
    computer_vision.obj_recog(cap)          # loop over or run as process/thread
    # CV.face_recog()         # necessary for individual frame processing
    computer_vision.haarcascade_test(cap)   # necessary to test haar cascades

    # 3
    comm_verify()
    arduino.positional_data()     # loop over pos_data, class variables get updated for speed & turning
    # 5
    arduino.speed()               # loop over speed
    arduino.turning()             # loop over turning


# test parallelism vs serial for end of program optimization
