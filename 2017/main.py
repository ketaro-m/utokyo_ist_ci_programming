import numpy as np
import os
from collections import deque
import utils

data_dir = os.path.join(os.path.dirname(__file__), 'data/')

def ans1(answering=True):
    if answering:
        print("No.1 Answer: 2 * (n * m * m)")
    return


def ans2(fname, answering=True):
    with open(data_dir+fname, mode='r') as f:
        s = f.read()
    s2 = s[:s.find('.')] # ignore after period
    mat = [i.split() for i in s2.split(',')] # split with comma, then split with space
    mat_array = np.array(mat, dtype='int')
    # print(mat)
    # print(mat_array)
    if answering:
        print("No.2 Answer: 2\n row: {}, column: {}".format(mat_array.shape[0], mat_array.shape[1]))
    return mat_array


def ans3(fname1, fname2, answering=True):
    a = ans2(fname1, answering=False)
    b = ans2(fname2, answering=False)
    c = a @ b
    # print(a)
    # print(b)
    # print(c)
    trace = np.trace(c)
    if answering:
        print("No.3 Answer:\n trace of C: {}".format(trace))


def ans4(m, n, s, answering=True):
    counter = 0 # answer for this problem
    pure_counter = 0 # answer for problem1
    a = np.zeros((m,n), dtype='int')
    b = np.zeros((n,m), dtype='int')
    c = np.zeros((m,m), dtype='int')

    cache = deque(maxlen=s) # FIFO queue to store indexes ex. 'a23', 'b00'
    for i in range(m):
        for j in range(m):
            d = 0
            for k in range(n):
                a_index = 'a'+str(i)+str(k)
                b_index = 'b'+str(k)+str(j)
                if a_index not in cache:
                    counter += 1
                    cache.append(a_index)
                if b_index not in cache:
                    counter += 1
                    cache.append(b_index)
                d += a[i][k] * b[k][j]
                pure_counter += 2
            c[i][j] = d
    # print(counter)
    # print(pure_counter)

    assert np.array_equal(c, a@b)

    if answering:
        print("No.4 Answer: {}".format(counter))
    return counter

""" return the minimum length of cache memory to minimize the times of accessing the main memory """
def ans4_ex(m,n):
    start_idx = n*2*m # the case all elements can be stored into cache memory
    count = ans4(m, n, start_idx, answering=False)
    count2 = count
    idx = 0
    while (count2 <= count):
        idx += 1
        count2 = ans4(m, n, start_idx-idx, answering=False)
    print("The minimum access times: {}, the next one: {}".format(count, count2))
    print("The minimum length of cache memory: {}".format(start_idx-idx+1))


def ans5(answering=True):
    if answering:
        print("No.5 Answer:\n (1,2,3,4) = (u,p,v,p,w,p)")
    return


def ans6(m, n, p, s, answering=True):
    assert m % p == 0, "m must be a product p"
    assert n % p == 0, "n must be a product p"
    counter = 0 # answer for this problem
    pure_counter = 0 # answer for problem1
    a = np.zeros((m,n), dtype='int')
    b = np.zeros((n,m), dtype='int')
    c = np.zeros((m,m), dtype='int')

    cache = deque(maxlen=s) # FIFO queue to store indexes ex. 'a23', 'b00'
    for u in range(0, m, p):
        for v in range(0, m, p):
            for w in range(0, n, p):
                for i in range(u, u+p, 1):
                    for j in range(v, v+p, 1):
                        d = 0
                        for k in range(w, w+p, 1):
                            a_index = 'a'+str(i)+str(k)
                            b_index = 'b'+str(k)+str(j)
                            if a_index not in cache:
                                counter += 1
                                cache.append(a_index)
                            if b_index not in cache:
                                counter += 1
                                cache.append(b_index)
                            d += a[i][k] * b[k][j]
                            pure_counter += 2
                        c[i][j] = d
    # print(counter)
    # print(pure_counter)

    assert np.array_equal(c, a@b)

    if answering:
        print("No.6 Answer: m={}, n={}, p={}, s={}, access={}".format(m, n, p, s, counter))
    return counter


def ans7(m, n, s, answering=True):
    p_list = utils.common_divisors(m, n)
    print(p_list)
    p_ans = 1
    min_times = float('inf')
    for p in p_list:
        times = ans6(m, n, p, s, answering=False)
        if times <= min_times:
            min_times = times
            p_ans = p
        print("m={}, n={}, p={}, s={}, access={}".format(m, n, p, s, times))
    if answering:
        print("No.7 Answer: p= {}, access= {}".format(p_ans, min_times))
    return p


def main():
    # ans1()
    # ans2('mat1.txt')
    # ans3('mat1.txt', 'mat2.txt')
    # ans4(50,10,0) # the same condition as problem 1
    # ans4(50, 10, 50*10*2) # the case all elements can be stored into cache memory
    # ans4_ex(50,10)
    # ans5()
    # ans4(50, 10, 50*10)
    # ans6(50, 10, 10, 50*10)
    ans7(200, 150, 600) # answer is p=10
    return



if __name__ == "__main__":
    main()