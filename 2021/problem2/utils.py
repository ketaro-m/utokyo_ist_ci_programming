import numpy as np


""" convert all the string elements of given list to int """
def strList2intList(str_ln: list):
    int_ln = [0] * len(str_ln)
    for i in range(len(str_ln)):
        int_ln[i] = int(str_ln[i])
    return int_ln




def file2numList(fname):
    with open(fname, mode='r') as f:
        s = f.read()
    num_str_ln = s.split(':')
    num_ln = strList2intList(num_str_ln)
    return num_ln


def ave(ln):
    ave_ln = [0] * len(ln)
    for i in range(3, len(ln)-3):
        ave_ln[i] = sum(ln[i-3:i+3]) / 7
    return ave_ln


def cor(ln1, ln2):
    m = len(ln1)
    n = len(ln2)
    if m < n:
        return
    arr1 = np.array(ln1)
    arr2 = np.array(ln2)
    cor_ln = np.zeros(m-n+1)
    for i in range(m-n+1):
        diff = arr1[i:i+n] - arr2
        cor_ln[i] = np.dot(diff, diff.T)
    # print(-min(cor_ln))
    return -min(cor_ln)


def calc_a(x):
    n = len(x)
    up1 = n * sum([i * x[i] for i in range(n)])
    up2 = sum([i * sum(x) for i in range(n)])
    bt1 = n * sum([i ** 2 for i in range(n)])
    bt2 = sum(range(n)) ** 2
    a = (up1 - up2) / (bt1 - bt2)
    return a


def calc_k(x):
    n = len(x)
    up1 = sum([i ** 2 * sum(x) for i in range(n)])
    up2 = sum([i * x[i] * sum(range(n)) for i in range(n)])
    bt1 = n * sum([i ** 2 for i in range(n)])
    bt2 = sum(range(n)) ** 2
    k = (up1 - up2) / (bt1 - bt2)
    return k


def calc_a2(x):
    n = len(x)
    up1 = n * sum([i * x[i] for i in range(n)])
    up2 = sum([i * sum(x) for i in range(n)])
    bt1 = n * sum([i ** 2 for i in range(n)])
    bt2 = sum(range(n)) ** 2
    a = (up1 - up2) / (bt1 - bt2)
    return a


def calc_k2(x):
    n = len(x)
    up1 = sum([i ** 2 * sum(x) for i in range(n)])
    up2 = sum([i * x[i] * sum(range(n)) for i in range(n)])
    bt1 = n * sum([i ** 2 for i in range(n)])
    bt2 = sum(range(n)) ** 2
    k = (up1 - up2) / (bt1 - bt2)
    return k

