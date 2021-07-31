import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy
import collections
import utils


def ans1(fname, answering=True):
    with open(fname, mode='r') as f:
        s = f.read()
    s_list = s.split()
    assert len(s_list) % 3 == 0, "data creation may have failed"
    pixel_num = int(len(s_list) / 3)
    if answering:
        print("No.1 Answer: pixel num =", pixel_num)

    pixels = []
    for i in range(pixel_num):
        pixels.append(utils.strList2intList(s_list[i*3:(i+1)*3]))
    return pixels


def ans2(fname, answering=True):
    pixel_list = ans1(fname, answering=False)
    # print(len(pixel_list))
    image_width = 0
    for i in range(len(pixel_list)):
        if sum(pixel_list[i]) == 255*3:
            if len(pixel_list) % (i+1) != 0:
                continue
            flag = True
            for j in range(int(len(pixel_list) / (i+1))):
                if sum(pixel_list[(i+1) * (j+1) - 1]) != 255*3:
                    flag = False
                    break
            if flag:
                image_width = i+1
                break
    if answering:
        print("No.2 Answer: image width =", image_width)
    return pixel_list, image_width


def ans3(fname, answering=True):
    pixel_list = ans1(fname, answering=False)
    n = len(pixel_list)
    assert n % 2 == 0, "pixel num must be even (if not, recreate data)"
    indices = list(reversed(range(len(pixel_list)))) # reverse in order to solve 
    # sort with the mount of fluorescence
    sorted_indices = sorted(indices, key=lambda index: sum([i**2 for i in pixel_list[index]]))
    middle_index = sorted_indices[int(n/2)]
    middle_fluorescence = pixel_list[middle_index]

    # # check
    # for i in range(-5,5):
    #     print("index", sorted_indices[int(n/2 + i)])
    #     print("pixel value", pixel_list[sorted_indices[int(n/2 + i)]])
    #     print("fluorescence", sum([j**2 for j in pixel_list[sorted_indices[int(n/2 + i)]]]))
    #     print()

    if answering:
        print("No.3 Answer: n/2 index =", middle_index, "fluorescence =", middle_fluorescence)
    return (pixel_list, sorted_indices)


def ans4(fname, k=4, answering=True):
    answer_indexes = []
    answer_pixels = []
    (pixel_list, sorted_indices) = ans3(fname, answering=False)
    n = len(pixel_list)
    assert n % k == 0, "n must be a multiple of k"
    for i in range(k):
        index = sorted_indices[int(n * i / k)]
        e_i = pixel_list[index]
        answer_indexes.append(index)
        answer_pixels.append(e_i)
        # print(int(n * i / k), index, e_i)
    
    if answering:
        print("No.4 Answer: ")
        for i in range(len(answer_pixels)):
            print("index: ", answer_indexes[i], ", value: ", answer_pixels[i])
    return answer_indexes, answer_pixels, pixel_list


def ans5(fname, k, answering=True):

    """ return a new array of cluster numbers for each pixels """
    def find_closest(pixels, representatives):
        # slow
        # cluster_num = np.ndarray(len(pixels)) # which representatives each pixels belong to (cluster num)
        # for j in range(len(pixels)):
        #     distance_array = np.flip(np.array([utils.distance_of_pixels(pixels[j], e[1]) for e in representatives])) # flip array to choose max index
        #     cluster_num[j] = np.argmin(distance_array)
        # return cluster_num

        distances = np.sum(abs(pixels - representatives[:, np.newaxis]), axis=2) # shape: (len(representatives), len(pixels))
        distances = np.flipud(distances) # flip array to choose max index
        cluster_num = np.argmin(distances, axis=0) # shape: (len(pixels),)
        return cluster_num

    """ return a new array of representatives (which index of pixels the representatives are) """
    def new_representatives(pixels, cluster_num):
        centroids = np.zeros([k,3])
        for i in range(k):
            centroids[i] = pixels[cluster_num==i].mean(axis=0)
        distances = np.sum(abs(pixels - centroids[:, np.newaxis]), axis=2) # shape: (len(representatives), len(pixels))
        distances = np.fliplr(distances)
        representative_indexes = np.argmin(distances, axis=1) # shape: (k,)
        return representative_indexes


    representative_indexes, _, pixel_list = ans4(fname, k, answering=False)
    # arraying
    pixel_array = np.array(pixel_list)
    representative_indexes_array = np.array(representative_indexes)
    # print(pixel_array.shape)
    # print(representative_indexes_array.shape)
    
    for _ in range(10):
        representative_pixels_array = pixel_array[representative_indexes_array]
        cluster_num = find_closest(pixel_array, representative_pixels_array)
        representative_indexes_array = new_representatives(pixel_array, cluster_num)
        print(_ + 1)
    
    representative_pixels_array = pixel_array[representative_indexes_array]
    # print(representative_pixels_array.shape)

    if answering:
        print("No.5 Answer: ")
        print("i=40: ", representative_pixels_array[40])
        print("i=80: ", representative_pixels_array[80])
        print("i=120: ", representative_pixels_array[120])
    return representative_indexes_array, cluster_num, pixel_array


""" check if ans5() is valid
the picture is the same as tif image by ans6() """
def ans5_sub(fname, k):
    representative_indexes_array, cluster_num, pixel_array = ans5(fname, k, answering=False)
    _, width = ans2(fname, answering=False)
    height = int(len(pixel_array) / width)
    plt.imshow(pixel_array[cluster_num].reshape(height, width, 3))
    plt.show()
    


def ans6(fname, k, answering=True):
    representative_indexes_array, cluster_num, pixel_array = ans5(fname, k, answering=False)
    _, width = ans2(fname, answering=False)
    height = int(len(pixel_array) / width)
    size = width * height * 3
    assert size == len(pixel_array) * 3, "size is incorrect"
    print(height, width, size)

    """ return a list of int of 4 bytes with big endian """
    def big4(num):
        return [(num >> (8*i)) & 0xff for i in reversed(range(4))]
    # # check
    # s = size.to_bytes(4, 'big')
    # print(s)
    # print(bytearray(big4(size)))
    
    w = big4(width)
    h = big4(height)
    s = big4(size)
    header = [
        77, 77, 0, 42, 0, 0, 0, 8, 0, 7, 1, 0, 0, 4, 0, 0,
        0, 1, w[0], w[1], w[2], w[3], 1, 1, 0, 4, 0, 0, 0, 1, h[0], h[1],
        h[2], h[3], 1, 2, 0, 3, 0, 0, 0, 3, 0, 0, 0, 98, 1, 6,
        0, 3, 0, 0, 0, 1, 0, 2, 0, 0, 1, 17, 0, 4, 0, 0,
        0, 1, 0, 0, 0, 104, 1, 21, 0, 3, 0, 0, 0, 1, 0, 3,
        0, 0, 1, 23, 0, 4, 0, 0, 0, 1, s[0], s[1], s[2], s[3], 0, 0,
        0, 0, 0, 8, 0, 8, 0, 8
    ]
    assert len(header) == 104

    values = list(pixel_array[cluster_num].flatten())
    result = []
    result.extend(header)
    result.extend(values)
    barray = bytearray(result)
    assert len(result) == size + 104, "mismatch in the length of the bytearray"
    with open(fname.replace('.txt', '.tif'), mode='wb') as f:
        f.write(barray)
    return



def main():
    # ans1("data/image1.txt")
    # ans2("data/image1.txt")
    # ans3("data/image1.txt")
    # ans4("data/image2.txt", k=4)
    # ans5("data/image2.txt", k=128)
    # ans5_sub("data/Lenna.txt", k=32)
    ans6("data/image2.txt", k=4)
    return



if __name__ == "__main__":
    main()