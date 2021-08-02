import numpy as np
import matplotlib.pyplot as plt
import main

""" return True if all the elements of two given lists are the same
usage : assert compare_lists(actual, expected) """
def compare_lists(actual, expected):
    return all([a == b for a, b in zip(actual, expected)])


""" compare two given text file """
def compare_textFiles(f1, f2):
    with open(f1, mode='r') as f:
        s1 = f.read()
    with open(f2, mode='r') as f:
        s2 = f.read()
    return s1 == s2


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


""" (non-destructive) remove all 0 row/column from the given array """
def del_allzero(arr, axis=0):
    obj = []
    for i in range(arr.shape[axis]):
        specif = arr[i,:] if axis==0 else arr[:,i]
        if np.all(specif == 0):
            obj.append(i)
    return np.delete(arr, obj, axis=axis)



""" convert numpy array into text """
def array2text(array):
    text_list = [''.join([num2str(n) for n in ln]) for ln in array]
    text = '\n'.join(text_list)
    return text


""" convert numpy array into text """
def text2array(text):
    text_list = text.splitlines() # list of each line
    text_list_2d = [[str2num(s) for s in line] for line in text_list]
    text_array = np.array(text_list_2d)
    return text_array


""" convert str to number
" " -> 0, , "|" -> 1, "*" -> 2 """
def str2num(s: str):
    assert s in [' ', '|', '*'], "invalid input"
    if s == ' ':
        return 0
    elif s == '|':
        return 1
    elif s == '*':
        return 2

""" convert character to number
" " -> 0, , "|" -> 1, "*" -> 2 """
def num2str(n: int):
    assert n in [0, 1, 2], "invalid input"
    if n == 0:
        return ' '
    elif n == 1:
        return '|'
    elif n == 2:
        return '*'


""" put num_array into arr at (i,j), returning the right-buttom index """
def put_array(arr, num_array, i, j):
    h = num_array.shape[0]
    w = num_array.shape[1]
    arr[i:i+h, j:j+w] = num_array
    return i+h, j+w



numArray_list = [
    np.array([
        [2,2,2,2],
        [1,0,0,1],
        [2,0,0,2],
        [1,0,0,1],
        [2,2,2,2]
        ]),
    np.array([
        [2],
        [1],
        [2],
        [1],
        [2]
        ]),
    np.array([
        [2,2,2,2],
        [0,0,0,1],
        [2,2,2,2],
        [1,0,0,0],
        [2,2,2,2]
        ]),
    np.array([
        [2,2,2,2],
        [0,0,0,1],
        [2,2,2,2],
        [0,0,0,1],
        [2,2,2,2]
        ]),
    np.array([
        [2,0,0,2],
        [1,0,0,1],
        [2,2,2,2],
        [0,0,0,1],
        [0,0,0,2]
        ]),
    np.array([
        [2,2,2,2],
        [1,0,0,0],
        [2,2,2,2],
        [0,0,0,1],
        [2,2,2,2]
        ]),
    np.array([
        [2,0,0,0],
        [1,0,0,0],
        [2,2,2,2],
        [1,0,0,1],
        [2,2,2,2]
        ]),
    np.array([
        [2,2,2,2],
        [0,0,0,1],
        [0,0,0,2],
        [0,0,0,1],
        [0,0,0,2]
        ]),
    np.array([
        [2,2,2,2],
        [1,0,0,1],
        [2,2,2,2],
        [1,0,0,1],
        [2,2,2,2]
        ]),
    np.array([
        [2,2,2,2],
        [1,0,0,1],
        [2,2,2,2],
        [0,0,0,1],
        [0,0,0,2]
        ]),
]


if __name__ == "__main__":
    with open('data/out1_dummy.txt', mode='r') as f:
        s = f.read()
    arr = text2array(s)
    print(arr)
    txt = array2text(arr)
    print(txt)
    assert s == txt
    print()