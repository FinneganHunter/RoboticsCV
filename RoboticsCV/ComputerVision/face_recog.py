import cv2 as cv
import numpy as np

face_data = {}


def multi_face(cap, escape_key='q'):  # does not work as intended

    face_cascades = {
        'face1': cv.CascadeClassifier('../resources/haar-cascade/haarcascade_frontalface_default.xml'),
        'face2': cv.CascadeClassifier('../resources/haar-cascade/haarcascade_frontalface_alt.xml'),
        'face3': cv.CascadeClassifier('../resources/haar-cascade/haarcascade_frontalface_alt2.xml'),
        'face4': cv.CascadeClassifier('../resources/haar-cascade/haarcascade_frontalface_alt_tree.xml'),
        'face5': cv.CascadeClassifier('../resources/haar-cascade/haarcascade_profileface.xml'),
    }
    dect_faces = []
    face_locations = []

    global face_data
    face_cascade = cv.CascadeClassifier('../resources/haar-cascade/haarcascade_frontalface_default.xml')

    print(f'escape key is {escape_key}')

    while True:

        ret, img = cap.read()
        gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # for i in face_cascades.values():
        #     dect_faces.append(i.detectMultiScale(gray_img, 1.3, 5)

        faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)

        # for i in range(len(dect_faces)):
        #    for (x, y, w, h) in dect_faces[i]:
        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # store x, y for each face cascade; compare values; average into master x,y
            """
            for i in range(len(dect_faces)): // 0, 1, 2, 3, 4, 5
                for (x, y, w, h) in dect_faces[i]:
                    face_locations[::-i][0] = x
                    face_locations[::-i][1] = y
                    
                    if face_location[i]
                    x_avg = 
                    y_avg = 
            """

            # roi_gray = gray_img[y:y + h, x:x + w]
            # roi_color = img[y:y + h, x:x + w]

            face_data = {'loc': {'x': int(x+w/2), 'y': int(y+h/2)}, 'dim': {'w': w, 'h': h}}

            # print('location: \t', str(face_data_dict['location']), '\tin image size:\t',  img.shape)

            height, width, channels = img.shape

            if face_data['loc']['x'] > width*3/5:
                print('you\'ve gone right')
            elif face_data['loc']['x'] < width*2/5:
                print('you\'ve gone left')
            if (face_data['dim']['w']+face_data['dim']['h'])/2 < width/3:
                print('you\'ve gone far away')
            # convert image data to motor controls


            # TODO: stores the location data for any number of simililar cascades, compares them all, finds ones ->
            # TODO: within a locational tolerance and averages them in that case
        # make it so they're just global variables that're changed -> done
        # or concurrent.futures module
        # print('rois:' + str(*roi_gray) + '\t' + str(*roi_color) + '\tin: ' + str(*img.shape))

        cv.imshow(f'face_recog feed - escape key is {escape_key}', img)
        if cv.waitKey(1) & 0xFF == ord(escape_key):  #
            break

    cap.release()
    cv.destroyAllWindows()
