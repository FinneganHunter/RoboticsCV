# TODO: Check to see if feature matching works on different sizes of images, or just exactly match the template

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)


def feature_match(frame_tf: bool):  # show frame of the function internal video feed  with a rectangle to show matches

    ret, tb_matched_rgb = cap.read()

    # tb_matched_rgb = cv.imread('template-matching-python-tutorial.jpg')   # this should be a frame in a video feed
    tb_matched_gray = cv.cvtColor(tb_matched_rgb, cv.COLOR_BGR2GRAY)    # convert to grayscale

    # TODO: create the template for matching
    template = cv.imread('.../resources/matching-template.png', 0)   # imports the template to be matched against
    width, height = template.shape[::-1]    # defines the width and height of the template, [::-1] last entries of array

    # implements template matching using cv.TM_CCOEFF_NORMED
    res = cv.matchTemplate(tb_matched_gray, template, cv.TM_CCOEFF_NORMED)  # template match
    threshold = 0.75

    # np.where -> tell me where in this array, entries satisfy a given condition
    loc = np.where(res >= threshold)   # generic definition of location of the result of the template match, array

    print(*loc)     # use this to try to understand what loc is with np.where

    if frame_tf:
        for pt in zip(*loc[::-1]):

            # cv.rectangle(image_to_draw_on, start_point(x, y), end_point(x, y), color(B,G,R), thickness(pt))
            cv.rectangle(tb_matched_rgb, pt, (pt[0] + width, pt[1] + height), (0, 255, 255), 2)

        cv.imshow('Detected', tb_matched_rgb)


def test_feature_match():

    while True:

        feature_match(True)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
