import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import copy
import collections
import utils

data_dir = os.path.join(os.path.dirname(__file__), 'data/')


def ans1(fname, answering=True):
    with open(fname, mode='r') as f:
        s = f.read()
    num_str_ln = s.split(':')
    num_ln = utils.strList2intList(num_str_ln)
    # print(num_ln)
    num_ln = list(set(num_ln)) # remove doubling
    num_ln.sort(reverse=True)
    # print(num_ln))
    ans_num = num_ln[9]
    if answering:
        print("No.1 Answer: {} ".format(ans_num))
    return ans_num


def ans2(answering=True):
    files = os.listdir(data_dir)
    files.sort()
    ans_ln = []
    for fname in files:
        ans_ln.append(ans1(data_dir+fname, answering=False))
    assert len(ans_ln) == len(files)
    ans_num = sum(ans_ln)
    if answering:
        print("No.2 Answer: {} ".format(ans_num))
    return


def ans3(fin, fout, answering=True):
    with open(fin, mode='r') as f:
        s = f.read()
    num_str_ln = s.split(':')
    num_ln = utils.strList2intList(num_str_ln)


    ans_ln = [utils.num2str_with_sign(num_ln[i] - num_ln[i-1]) for i in range(1, len(num_ln))]
    ans_str = ''.join(ans_ln)

    if answering:
        print("No.3 Answer:\n output string : {}\n length : {}".format(ans_str, len(ans_str)))
        with open(fout, mode='w') as f:
            f.write(ans_str)
    return ans_str



def ans4(fname, answering=True):
    with open(fname, mode='r') as f:
        s = f.read()
    num_str_ln = s.split(':')
    num_ln = utils.strList2intList(num_str_ln)
    diff_ln = [(num_ln[i] - num_ln[i-1]) for i in range(1, len(num_ln))]

    positve_diff_index = utils.positive_index(diff_ln)
    positve_diff_index_consecutive = utils.consecutive_list(positve_diff_index)

    # print(diff_ln)
    # print(positve_diff_index_consecutive)

    max_diff_sum = 0
    max_len = 0
    result = []
    diff_array = np.array(diff_ln)
    for ln in positve_diff_index_consecutive:
        ln_array = np.array(ln)
        possible_max_diff_sum = sum(diff_array[ln_array])
        if possible_max_diff_sum > max_diff_sum:
            max_diff_sum = possible_max_diff_sum
            max_len = len(ln_array)
            result = [ln_array]
        elif possible_max_diff_sum == max_diff_sum:
            if len(ln_array) < max_len:
                result = [ln_array]
            elif len(ln_array) == max_len:
                result.append(ln_array)
            else:
                pass


    if answering:
        print("No.4 Answer: {} ".format(result))
    return

def main():
    ans1('infections.txt')
    ans2()
    ans3('infections.txt', 'diff.txt')
    
    ans4('infections.txt')
    return



if __name__ == "__main__":
    main()