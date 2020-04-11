from RoboticsCV import ComputerVision
# from gpiozero import PWMLED

# https://gpiozero.readthedocs.io/en/stable/api_output.html#pwmoutputdevice


def comm_verify():
    try:
        # TODO: send ping & receive ping on each of the 4 pins
        print("see RoboticsCV.Image-Proc.class_test TODO")

    except IOError as e:
        print(str(e))


class ArduinoCommClass:

    def __init__(self, pin1, pin2, pin3, pin4):
        """pins for the arduino communication"""

        # TODO: make the pins a function in arduino_comm which are passed from app, setup function or class

        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4

        self.pin_nums = [self.pin1, self.pin2, self.pin3, self.pin4]

        # Direction pins
        # self.x_axis_positive = PWMLED(pin_numbers[0])
        # self.x_axis_negative = PWMLED(pin_numbers[1])

        # Speed pins
        # self.y_axis_positive = PWMLED(pin_numbers[2])
        # self.y_axis_negative = PWMLED(pin_numbers[3])

    def positional_data(self):

        roi = ComputerVision.haarcascade_test()

        self.frame_x_position = 0  # will update from roi, position of roi in camera frame
        self.frame_depth_position = 0  # will update from roi, dimensions of roi
        self.frame_x_baseline = 0
        self.frame_depth_baseline = 0

        return self.frame_x_position, self.frame_depth_position

    def turning(self):
        """if object is un-centered, turn left or right"""

        x_delta = self.frame_x_position - self.frame_x_baseline
        # x_value = self.frame_x_position - self.frame_x_baseline

        # TODO: change these functions to have x_position_delta be turn_delta and have speed based off it
        if x_delta > 5:
            # turn right
            print("write increasing x_positive_axis values to object based on passed frame value")
            # self.x_axis_positive.value(x_value)

        if x_delta < -5:
            # turn left
            print("write increasing x_negative_axis values to object based on passed frame value")
            # self.x_axis_negative.value(x_value)

    def speed(self):
        """if frame get distance away, increase speed, vice-versa"""

        depth_delta = self.frame_depth_position - self.frame_depth_baseline
        # depth_value = self.frame_depth_position - self.frame_depth_baseline

        if depth_delta > 5:
            # go forward
            print("write increasing y_positive_axis values to object based on passed frame size")
            # self.y_axis_positive.value(depth_value)

        if depth_delta < -5:
            # go backwards
            print("write increasing y_positive_axis values to object based on passed frame size")
            # self.y_axis_positive.value(depth_value)
