import numpy as np
import matplotlib.pyplot as plt
import os
import utils

data_dir = os.path.join(os.path.dirname(__file__), 'data/')


def pr2():
    mat1_txt = "0 1 2 3,4 5 6 7,8 9 10 11.12 13 14 15 16,17 18 19 20 21,22,23"
    with open(data_dir+'mat1.txt', mode='w') as f:
        f.write(mat1_txt)
    return

def pr3():
    mat2_txt = "3 2 1,4 5 6,11 10 9,12 13 14.12 13 14 15 16,17 18 19 20 21,22,23"
    with open(data_dir+'mat2.txt', mode='w') as f:
        f.write(mat2_txt)
    return


if __name__ == "__main__":
    pr2()
    pr3()
    print(0)