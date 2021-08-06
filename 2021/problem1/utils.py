import numpy as np


""" convert all the string elements of given list to int """
def strList2intList(str_ln: list):
    int_ln = [0] * len(str_ln)
    for i in range(len(str_ln)):
        int_ln[i] = int(str_ln[i])
    return int_ln


""" convert num to str with sign '+' or '-' """
def num2str_with_sign(num):
        if num >= 0:
            return '+' + str(num)
        else:
            return str(num)


def positive_index(ln):
    result = []
    for i in range(len(ln)):
        if ln[i] > 0:
            result.append(i)
    return result


""" ex. [2,3,4,6,7,10,11,12] -> [[2,3,4], [6,7], [10,11,12]] """
def consecutive_list(ln: list):
    split_list = []
    small_list = []
    pre = float('inf')
    for v in ln:
        if v == pre + 1:
            small_list.append(v)
        else:
            if len(small_list):
                split_list.append(small_list)
            small_list = [v]
        pre = v
    split_list.append(small_list)
    return split_list
