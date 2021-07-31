import numpy as np
import matplotlib.pyplot as plt
import main

""" return True if all the elements of two given lists are the same
usage : assert compare_lists(actual, expected) """
def compare_lists(actual, expected):
    return all([a == b for a, b in zip(actual, expected)])


""" convert all the string elements of given list to int """
def strList2intList(str_ln: list):
    int_ln = [0] * len(str_ln)
    for i in range(len(str_ln)):
        int_ln[i] = int(str_ln[i])
    return int_ln


""" return the distance of two given pixel, for problem5
distance of [ri, gi, bi] and [rj, gj, bj] is |ri-rj|+|gi-gj|+|bi-bj| """
def distance_of_pixels(pixel_i: list, pixel_j: list):
    assert len(pixel_i) == 3 and len(pixel_j) == 3, "pixel must be a list of three elements [r, g, b]"
    return sum([abs(pixel_i[i] - pixel_j[i]) for i in range(len(pixel_i))])



""" plot image from text file """
def plot_txt(fname):
    pixel_list, width = main.ans2(fname)
    height = int(len(pixel_list) / width)
    pixel_array = np.array(pixel_list)
    pixel_array = pixel_array.reshape(height, width, 3)
    plt.imshow(pixel_array)
    plt.show()
    return pixel_array


if __name__ == "__main__":
    print()