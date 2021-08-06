import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import itertools
import copy
import collections
import utils

data_dir = os.path.join(os.path.dirname(__file__), 'data/')


def ans0(fname, answering=True):
    with open(fname, mode='r') as f:
        s = f.read()
    ans_num = 0
    if answering:
        print("No.0 Answer: {} ".format(ans_num))
    return ans_num

def ans1(fname, answering=True):
    num_ln = utils.file2numList(fname)
    ave_ln = utils.ave(num_ln)
    min_num = min(ave_ln[3:-3])
    max_num = max(ave_ln[3:-3])
    sum_num = sum(ave_ln[3:-3])
    if answering:
        print("No.1 Answer: min = {:.5f}, max = {:.5f}, sum = {:.5f} ".format(min_num, max_num, sum_num))
    return ave_ln


def ans2(answering=True):
    files = os.listdir(data_dir)
    files.sort()

    max_s = -float('inf')
    max_s_pairs = []
    for f in itertools.permutations(files, 2):
        #print(v)
        num_ln1 = utils.file2numList(data_dir+f[0])
        num_ln2 = utils.file2numList(data_dir+f[1])
        s = utils.cor(num_ln1, num_ln2)
        if s == None:
            continue

        if s > max_s:
            max_s = s
            max_s_pairs = [f]
            # print(min_s_pairs)
        elif s == max_s:
            max_s_pairs.append(f)
            # print(min_s_pairs)
            
    if answering:
        print("No.2 Answer: s = {}, file_pairs = {}".format(max_s, max_s_pairs))
    return


def ans3(fname, answering=True):
    num_ln = utils.file2numList(fname)
    
    a = utils.calc_a(num_ln)
    k = utils.calc_k(num_ln)
    if answering:
        print("No.3 Answer: a = {:.5f}, k = {:.5f}".format(a, k))
    return a, k


def ans4(fname, answering=True):
    num_ln = utils.file2numList(fname)

    max_a = -float('inf')
    max_a_pairs = []
    for s in range(len(num_ln) - 30):
        partial_num_ln = num_ln[s:s+30]
        # print(len(partial_num_ln))
        a = utils.calc_a2(partial_num_ln)
        k = utils.calc_k2(partial_num_ln)
        if a > max_a:
            max_a = a
            max_a_pairs = [[s, a, k]]
        elif a == max_a:
            max_a_pairs.append([s, a, k])
            # print(min_s_pairs)
            

    if answering:
        print("No.4 Answer: {}".format(max_a_pairs))
    return a, k


def main():
    ans1('infections.txt')
    ans2()
    ans3('infections2.txt')
    ans4('infections2.txt')
    return



if __name__ == "__main__":
    main()