"""
from gpiozero import PWMLED
#from ..app import pin_assign
from .. import ComputerVision

# https://gpiozero.readthedocs.io/en/stable/api_output.html#pwmoutputdevice

# TODO: make the pins a function in arduino_comm which are passed from app, setup function or class


def pin_assign(pin1, pin2, pin3, pin4) -> list:
    return [pin1, pin2, pin3, pin4]


pin_numbers = pin_assign(5, 6, 13, 19)  # should return as a list so changes can be done in app.py


roi = ComputerVision.haarcascade_test()

# Direction pins
x_axis_positive = PWMLED(pin_numbers[0])
x_axis_negative = PWMLED(pin_numbers[1])

# Speed pins
y_axis_positive = PWMLED(pin_numbers[2])
y_axis_negative = PWMLED(pin_numbers[3])

# TODO: update variables from CV, placeholders below, loc variable

frame_x_position = 0
frame_depth_position = 0
frame_x_baseline = 0
frame_depth_baseline = 0

turn_delta = frame_x_position - frame_depth_baseline
depth_delta = frame_depth_position - frame_depth_baseline


# .value() parameters go from 0 to 1, for variable PWM signal
# the higher value away from baseline depth and center, the closer to 1 gets passed
# within baseline, 0 gets passed


# TODO: if object is un-centered, turn left or right
def turning(x_position: int):
    if x_position > 5:
        # turn right
        print("write increasing x_positive_axis values to object based on passed frame value")
        x_axis_positive.value(turn_delta)

    if x_position < -5:
        # turn left
        print("write increasing x_negative_axis values to object based on passed frame value")
        x_axis_negative.value(turn_delta)


# TODO: if frame get distance away, increase speed, vice-versa
def speed(depth_value: int):
    if depth_value > 5:
        # go forward
        print("write increasing y_positive_axis values to object based on passed frame size")
        y_axis_positive.value(depth_delta)

    if depth_value < -5:
        # go backwards
        print("write increasing y_positive_axis values to object based on passed frame size")
        y_axis_positive.value(depth_delta)
#"""