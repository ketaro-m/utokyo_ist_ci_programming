import numpy as np
import matplotlib.pyplot as plt
import random
import os
import cv2
from numpy.core.fromnumeric import reshape
import utils
import main
import time

data_dir = os.path.join(os.path.dirname(__file__), 'data/')


def pr1():
    random.seed(0)
    image_height = random.randint(2,1024)
    image_width = random.randrange(2,512) * 2 # for problem3's condition
    print("image size (h x w): ", (image_height, image_width))
    data_list = []
    for _ in range(image_height):
        for i in range(image_width):
            # right edge is white
            if i == image_width - 1:
                data_list.extend(["255","255","255"])
                continue
            for _ in range(3):
                data_list.append(str(random.randrange(256)))
    data_str = ' '.join(data_list)
    with open(data_dir+'image1.txt', mode='w') as f:
        f.write(data_str)



def pr4(k=4):
    random.seed(1)
    image_height = random.randint(2,128) * 8
    image_width = random.randrange(2,64) * 16 # for problem5's condition
    print("image size (h x w): ", (image_height, image_width))
    data_list = []
    for _ in range(image_height):
        for i in range(image_width):
            # right edge is white
            if i == image_width - 1:
                data_list.extend(["255","255","255"])
                continue
            for _ in range(3):
                data_list.append(str(random.randrange(256)))
    data_str = ' '.join(data_list)
    with open(data_dir+"image2.txt", mode='w') as f:
        f.write(data_str)


def pr5(k=4):
    random.seed(1)
    image_height = random.randint(2,1024)
    image_width = random.randrange(2,512) * k # for problem3's condition
    print("image size (h x w): ", (image_height, image_width))
    data_list = []
    for _ in range(image_height):
        for i in range(image_width):
            # right edge is white
            if i == image_width - 1:
                data_list.extend(["255","255","255"])
                continue
            for _ in range(3):
                data_list.append(str(random.randrange(256)))
    data_str = ' '.join(data_list)
    with open(data_dir+"image2.txt", mode='w') as f:
        f.write(data_str)


def pr6():
    image2txt('Lenna_raw.png')
    utils.plot_txt(data_dir+'Lenna.txt') # check
    image2txt('sherlock_raw.jpg')
    utils.plot_txt(data_dir+'sherlock.txt') # check
    image2txt('profile_raw.jpg')
    utils.plot_txt(data_dir+'profile.txt') # check
    return


""" convert image file to text file making the right edge white (255, 255, 255) """
def image2txt(fname):
    img = cv2.imread(data_dir+fname)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    img_array = np.asarray(img)
    print(img_array.shape)
    
    """ print(img_array.flatten().shape) """
    img_array[:,-1,:] = 255 # make the right edge white
    data_list = list(img_array.flatten().astype('str'))
    data_string = ' '.join(data_list)
    with open(data_dir+fname.replace('_raw.png', '.txt').replace('_raw.jpg','.txt'), mode='w') as f:
        f.write(data_string)
    return


if __name__ == "__main__":
    # pr1()
    # pr4()
    # pr5()
    pr6()
    print(0)