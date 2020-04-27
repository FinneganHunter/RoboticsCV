from RoboticsCV import ComputerVision
from gpiozero import PWMLED as PWM, LED as OUT_PIN, DigitalInputDevice as IN_PIN


class ArduinoCommClass:
    """Class for arduino IO & communication"""

    def __init__(self, pin1, pin2, pin3, pin4):
        """pins for the arduino communication"""

        # TODO: make the pins a function in arduino_comm which are passed from app, setup function or class

        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4

        self.pin_nums = [self.pin1, self.pin2, self.pin3, self.pin4]

        """
        # Direction pins
        self.x_axis_positive = PWM(self.pin_nums[0])
        self.x_axis_negative = PWM(self.pin_nums[1])

        # Speed pins
        self.y_axis_positive = PWM(self.pin_nums[2])
        self.y_axis_negative = PWM(self.pin_nums[3])
        """

    # TODO: make this test the actual class defined communication pins on the arduino, redundant otherwise
    def comm_verify(self, pin5: int) -> None:
        """Verifies communication between arduino and computer"""

        from time import sleep

        # declare the receiving pin an a GPIO input device
        self.recv_pin = IN_PIN(pin5)

        try:
            for i in self.pin_nums:
                # TODO: send ping & receive ping on each of the 4 pins
                print("see RoboticsCV.Image-Proc.class_test TODOs")

                pin = OUT_PIN(i)
                pin.on()

                self.recv_pin.wait_for_active(3)
                raise IOError if not self.recv_pin.value else print(f'pin{i} communication verified')

        except IOError:
            print('pin communication failure')

    def positional_data(self, roi: list, dim: tuple):
        """Sets the 'x' and 'depth' positions and baselines"""
        """roi is face data, baseline is dim from .shape"""

        self.frame_x_position = roi[0][0]  # will update from roi, position of roi in camera frame
        self.frame_depth_position = (roi[1][0] + roi[1][1]) / 2  # will update from roi, dimensions of roi

        self.frame_x_baseline = dim[0] / 2  # 1920/2
        self.frame_depth_baseline = dim[1] / 3  # 1080/3

    # convert image data to motor controls
    # print('you\'ve gone right') if face_data['loc']['x'] > width*3/5:
    # print('you\'ve gone left') if face_data['loc']['x'] < width*2/5:
    # print('you\'ve gone far away') if (face_data['dim']['w'] + face_data['dim']['h'])/2 < width/3:
    # https://www.gpiozero.readthedocs.io/en/stable/source_values.html

    def turning(self):
        """sends turn commands to arduino"""
        """if object is un-centered, turn left or right"""

        x_delta = self.frame_x_position - self.frame_x_baseline
        x_value = 0

        # TODO: change these functions to have x_position_delta be turn_delta and have speed based off it
        if x_delta > 50:
            # turn right
            print("write increasing x_positive_axis values to object based on passed frame value")
            self.x_axis_positive.source(x_value)  # map between 0 and 1

        if x_delta < -50:
            # turn left
            print("write increasing x_negative_axis values to object based on passed frame value")
            self.x_axis_negative.source(x_value)

    def movement(self):
        """send movement commands to arduino"""
        """if frame get distance away, increase speed, vice-versa"""

        depth_delta = self.frame_depth_position - self.frame_depth_baseline
        depth_value = 0

        if depth_delta > 50:
            # go forward
            print("write increasing y_positive_axis values to object based on passed frame size")
            self.y_axis_positive.source(depth_value)

        if depth_delta < -50:
            # go backwards
            print("write increasing y_positive_axis values to object based on passed frame size")
            self.y_axis_negative.source(depth_value)
