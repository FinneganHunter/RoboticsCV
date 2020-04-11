"""
Module that creates a new haar cascade by:
    scrapes an image database and store negative images,
    removes broken images,
    creates a descriptor,
    & launches the windows training gui

    ImageProc/image-proc.py .haarcascade_builder()
"""

import urllib.request
import cv2 as cv
# import numpy as np
import os


# TODO: add in deliniation for positive or negative scraping in raw image storage, all the features could be packed as gui options


def store_images(images_link: str, file_type=".jpg", custom_prefix="", n_p="neg",
                 file_location='.../resources/haar-cascade/'):
    file_location = file_location + n_p + "-dir"
    print(images_link)      # specify urls for website scrape
    print(file_type)        # specify the file type to save images as
    print(custom_prefix)    # designate your own custom prefix
    print(n_p)              # choose neg. or pos. to scrape -> changes all function, file, and other names in func
    print(file_location)    # choose a file location

# make this module into a class so that class variables can me manipulated across an object instance


# TODO: insert input matching function Here -> repl.it/repls/GainsboroHonorablePolygons

pic_num = 1


def store_raw_images(neg_images_link: str):

    global pic_num
    neg_images_urls = urllib.request.urlopen(neg_images_link).read().decode()

    if not os.path.exists('.../resources/haar-cascade/neg-dir'):
        os.makedirs('.../resources/haar-cascade/neg-dir')
    print('directory for negative images: \n.../resources/haar-cascade/neg-dir')

    neg_name = "neg/" + str(pic_num) + ".jpg"

    for i in neg_images_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, neg_name)
            img = cv.imread(neg_name, cv.IMREAD_GRAYSCALE)
            resized_image = cv.resize(img, (100, 100))
            cv.imwrite(neg_name, resized_image)
            pic_num += 1

        except Exception as exc:
            print(str(exc))

    print("image scrape and save complete")


# TODO: implement an outlier remover using template matching in broken_removal

def broken_removal(scan_delete=False):
    """Scans through directory and prints the broken images, True deletes them"""

    from PIL import Image

    for filename in os.listdir('.../resources/haar-cascade/neg-dir'):
        if filename.endswith('.jpg'):
            try:
                img = Image.open('.../resources/haar-cascade/neg-dir')
                img.verify()
            except (IOError, SyntaxError):
                print('Bad File ', filename)
                if not scan_delete:
                    os.remove(filename)


def descriptor_creator():

    for file_type in ['.../resources/haar-cascade/neg-dir']:
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type + '/' + img + ' 1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)

            elif file_type == 'neg':
                line = file_type + '/' + img + '\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)


def cascade_trainer_opener():

    import subprocess
    import webbrowser as web

    val = input('Do you have the cascade trainer? (y / n) ')

    while val != 'y' or val != 'Y':
        specific_url = 'https://amin-ahmadi.com/cascade-trainer-gui/'
        web.open(specific_url)

        val = input('do you have the cascade trainer installed? (y / n) ')

    print('allow cascade trainer to open')

    subprocess.Popen([r"C:\Program Files (x86)\Cascade Trainer GUI\Cascade-Trainer-GUI.exe"])


def haarcascade_builder():
    neg_database_links = ["//image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513",
                          "//image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152"
                          ]
    global pic_num

    store_raw_images(neg_database_links[1])
    print('first image scrape done')

    # this is where the file cleaner would go
    # broken_removal(True)
    print('broken files removed')

    store_raw_images(neg_database_links[2])
    print('second image scrape done \nnumber of images scraped: ' + str(pic_num))

    descriptor_creator()
    print('descriptor created')

    # make an info directory in resources
    if not os.path.exists('.../resources/haar-cascade/info'):
        os.makedirs('.../resources/haar-cascade/info')
        print('info folder created')

    cascade_trainer_opener()
    print('cascade trainer opened')

    return 'what will eventually be the directory of the cascade'
