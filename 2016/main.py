import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import copy
import collections 
import utils

data_dir = os.path.join(os.path.dirname(__file__), 'data/')


def ans1(num: int, answering=True):
    splits = [0 if i % 2 == 0 else 2 for i in range(len(str(num))*2-1)]
    text = ans3(num, splits, fname='out1.txt', answering=False)

    if answering:
        print("No.1 Answer:")
        print(text)
    return text


def ans2(fname='out1.txt', answering=True):
    num = ans4(fname=fname, answering=False)
    if answering:
        print("No.2 Answer: {}".format(num))
    return num


def ans3(num: int, splits: list, fname='out3.txt', answering=True):
    assert len(splits) == len(str(num)) * 2 - 1, "Invalid input"

    # calculate the height and the width of the array
    height = 5 + max(splits[::2])
    one_num = str(num).count('1') # how many '1' in num
    width = (len(str(num)) - one_num) * 4 + one_num * 1 + sum(splits[1::2])
    array = np.zeros((height, width))

    splits2 = [0] + splits
    column = 0
    for i in range(len(str(num))):
        c = str(num)[i]
        num_arr = utils.numArray_list[int(c)]
        _, column = utils.put_array(array, num_arr, splits2[i*2+1], column+splits2[i*2])

    text = utils.array2text(array)

    with open(data_dir+fname, mode='w') as f:
        f.write(text)

    if answering:
        print("No.3 Answer:")
        print(text)
    return text


def ans4(fname='out3.txt', answering=True, ans5=False):
    with open(data_dir+fname, mode='r') as f:
        s = f.read()
    arr = utils.text2array(s)

    columns = []
    for col in range(arr.shape[1]):
        if not np.all(arr[:,col] == 0):
            columns.append(col)
    columns_2d = utils.consecutive_list(columns)

    num_str = ""
    num_arrays = []
    for ln in columns_2d:
        num_arr = utils.del_allzero(arr[:,ln], axis=0) # do nothing if ans2()
        num_arrays.append(num_arr)
        for i in range(len(utils.numArray_list)):
            if np.array_equal(num_arr, utils.numArray_list[i]):
                num_str += str(i)
                break
    
    # for ans5() to use the preprocessing
    if ans5:
        return num_arrays


    assert len(num_str) == len(columns_2d), "recognition failed"

    num = int(num_str)
    if answering:
        print("No.4 Answer: {}".format(num))
    return num 


""" judge with square error """
def ans5(answering=True):
    num_arrays = ans4(fname='out5.txt', ans5=True)
    num_str = ""
    for num_arr in num_arrays:
        # 1 can be judge with its width
        if num_arr.shape[1] <= 2:
            num_str += '1'
            continue

        mse = float('inf')
        mse_num = 0
        for i in range(len(utils.numArray_list)):
            if i == 1: continue # skip the case num == 1
            assert num_arr.shape == utils.numArray_list[i].shape

            diff = (num_arr - utils.numArray_list[i])
            diff[diff!=0] = 1 # consider the all error as 1
            se = sum(sum(diff**2))
            if se < mse:
                mse = se
                mse_num = i
        num_str += str(mse_num)

    num = int(num_str)
    if answering:
        print("No.5 Answer: {}".format(num))
    return num 


def main():
    ans1(813)
    # assert utils.compare_textFiles(data_dir+'out1.txt', data_dir+'out1_ans.txt')
    ans2()
    ans3(813,[0,4,1,3,2])
    # assert utils.compare_textFiles(data_dir+'out3.txt', data_dir+'out3_ans.txt')
    ans4()
    ans5()
    return



if __name__ == "__main__":
    main()