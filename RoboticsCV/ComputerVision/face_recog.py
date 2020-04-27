import cv2 as cv
import numpy as np

width, height = 0, 0
face_data = []


def set_wh(cap) -> None:
    """sets the global variables for image width and height"""
    global height, width

    ret, img = cap.read()
    height, width, null = img.shape


# repl.it/repls/DarkgreenPersonalCoordinate
def reject_outliers(data: list, m: float = 1.0) -> np.array:
    """Removes the outliers from a data-set in a 1D list"""
    data = np.array(data)
    return data[abs(data - np.mean(data) < m * np.std(data))]


def multi_face_loop(cap, escape_key='q'):  # does not work as intended
    """Detects faces using multiple cascades, """

    global face_data

    face_cascades = [
        cv.CascadeClassifier('../resources/haar-cascade/haarcascade_frontalface_default.xml'),
        cv.CascadeClassifier('../resources/haar-cascade/haarcascade_frontalface_alt.xml'),
        cv.CascadeClassifier('../resources/haar-cascade/haarcascade_frontalface_alt2.xml'),
        cv.CascadeClassifier('../resources/haar-cascade/haarcascade_frontalface_alt_tree.xml'),
        cv.CascadeClassifier('../resources/haar-cascade/haarcascade_profileface.xml'),
        cv.CascadeClassifier('../resources/haar-cascade/haarcascade_profileface.xml'),
    ]

    for i in face_cascades:

        while True:

            ret, img = cap.read()
            gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            faces = i.detectMultiScale(gray_img, 1.3, 5)

            detected = 0 if not len(faces) else 1

            if detected:

                for (x, y, w, h) in faces:

                    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

                    face_dict = {'loc': {'x': int(x+w/2), 'y': int(y+h/2)}, 'dim': {'w': w, 'h': h}}
                    face_data = list(face_dict['loc'].values()), list(face_dict['loc'].values())
                    """
                    height, width = gray_img.shape
                    # convert image data to motor controls
                    if face_data['loc']['x'] > width*3/5:
                        print('you\'ve gone right')
                    elif face_data['loc']['x'] < width*2/5:
                        print('you\'ve gone left')
                    if (face_data['dim']['w'] + face_data['dim']['h'])/2 < width/3:
                        print('you\'ve gone far away')
                    """

            cv.imshow(f'face_recog feed - escape key is {escape_key}', img)

            if not detected:
                break
            if cv.waitKey(1) & 0xFF == ord(escape_key):
                break

    cap.release()
    cv.destroyAllWindows()


onerun_flag = False

def single_face(cap):
    """facial tracking with single cascade implemented"""

    global face_data, onerun_flag

    face_data = [0, 0], [0, 0] if not onerun_flag else None
    one_run_flag = True

    face_cascade = cv.CascadeClassifier('../resources/haar-cascade/haarcascade_frontalface_default.xml')

    # print(f'escape key is {escape_key}')

    ret, img = cap.read()
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)

    if len(faces) >= 1:
        for (x, y, w, h) in faces:

            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            face_dict = {'loc': {'x': int(x+w/2), 'y': int(y+h/2)}, 'dim': {'w': w, 'h': h}}
            face_data = list(face_dict['loc'].values()), list(face_dict['loc'].values())
            """
            height, width = gray_img.shape
            # convert image data to motor controls
            if face_data['loc']['x'] > width*3/5:
                print('you\'ve gone right')
            elif face_data['loc']['x'] < width*2/5:
                print('you\'ve gone left')
            if (face_data['dim']['w'] + face_data['dim']['h'])/2 < width/3:
                print('you\'ve gone far away')
            """
    else:

        print('no face detected')

            # the 3/4 view never lines up with the frontal image so no need to program overlap
    cv.imshow(f'face_recog feed', img)
