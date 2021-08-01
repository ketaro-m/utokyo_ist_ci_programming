import numpy as np
import random
import os
import utils
import time

data_dir = os.path.join(os.path.dirname(__file__), 'data/')

def pr1():
    random.seed(0)
    LENGTH = int(400 / 6)

    txt = ""
    for _ in range(LENGTH):
        binary = ""
        for _ in range(6):
            binary += str(random.choice([0, 1]))
        txt += utils.binary2code(binary)

    print(txt)
    with open(data_dir+'data1.txt', mode='w') as f:
        f.write(txt)


""" check with `$ hexdump data2a.bin` etc """
def pr2():
    a = ("data2a.bin", [0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x00, 0x06, 0x05, 0x48])
    data2a_ans = ("data2a.bin", [0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x42, 0x43, 0x44, 0x45, 0x46, 0x48])
    b = ("data2b.bin", [0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x00, 0x06, 0x05, 0x48])
    c = ("data2c.bin", [0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x00, 0x06, 0x05, 0x48])

    for f_ln in (a, b, c):
        # print(len(f_ln[1]))
        barray = bytearray(f_ln[1])
        print(barray)
        with open(data_dir + f_ln[0], mode='wb') as f:
            f.write(barray)


def pr3():
    a = ("data3a.txt", [0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x42, 0x43, 0x44, 0x45, 0x46, 0x48])
    a_ans = ("data3a_ans.bin", [0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x00, 0x06, 0x05, 0x48])
    b = ("data3b.png", [0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x41, 0x42, 0x43, 0x44, 0x46, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48])
    b_ans = ("data3b_ans.bin", [0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x00, 5, 5, 0x47, 0x00, 12, 4, 0x46, 0x00, 17, 6, 0x47, 0x48])
    for f_ln in (a, a_ans, b, b_ans):
        # print(len(f_ln[1]))
        barray = bytearray(f_ln[1])
        print(barray)
        with open(data_dir + f_ln[0], mode='wb') as f:
            f.write(barray)


def pr4():
    """ create answer plane and dict text file """
    fnames = ["data4_jobs_raw.txt", "data4_kingjr_raw.txt", "data4_lincoln_raw.txt", "data4_USconstitute_raw.txt"]
    random_seed_index = 0
    for fn in fnames:
        """ create answer place text """
        with open(data_dir + fn, mode='r') as f:
            s = f.read()
        s = ' '.join(s.splitlines())

        s = ''.join(char for char in s if (char.isalnum() or char==' ' or char=='.'))
        s = ''.join([i for i in s if not i.isdigit()]) # remove numbers
        s = s.lower()
        s = s.replace('  ', ' ')
        with open(data_dir + fn.replace('_raw', '_ans'), mode='w') as f:
            f.write(s)

        """ creat dict text """
        words = s.replace('.', '').split()
        dictionary = list(dict.fromkeys(words))
        # for w in words:
        #     if w not in dictionary:
        #         dictionary.append(w)
        dictionary.sort()
        dict_str = " ".join(dictionary)
        with open(data_dir + fn.replace('_raw', '_dict'), mode='w') as f:
            f.write(dict_str)

        """ Encryption """
        random.seed(random_seed_index)
        random_seed_index += 1
        encryption_map = [0]*28 # a~z, period, space,
        tmp_ln = list(range(len(encryption_map)))
        for i in range(len(encryption_map)):
            converted_num = random.choice(tmp_ln)
            encryption_map[i] = converted_num
            tmp_ln.remove(converted_num)
        # print(sorted(encryption_map))
        enc_str = ""
        for c in s:
            enc_str += utils.num2alphabet(encryption_map[utils.alphabet2num(c)])

        assert len(s) == len(enc_str), "length between encryption differs"
        with open(data_dir + fn.replace('_raw', ''), mode='w') as f:
            f.write(enc_str)
    


def pr5():
    a = ("data5_ex.bin", [0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48])
    barray = bytearray(a[1])
    with open(data_dir + a[0], mode='wb') as f:
        f.write(barray)

    def encryption(fname):
        e = 551263368336670859257571
        n = 3858843578360632069557337
        with open(fname, mode='rb') as f:
            s = f.read()
        assert len(s) % 4 == 0, "binary file must have 4xn bytes"
        result = []
        for i in range(int(len(s) / 4)):
            four_bytes = s[i*4:(i+1)*4]
            m = 0
            for k in range(4):
                m += 2**(8*(3-k)) * four_bytes[k]
            print(m % n)
            print("calculating c")
            c = 1
            for _ in range(e):
                c *= (m % n)
                c %= n
            # c = ((m % n) ** e) % n
            print("calculation end")
            result.append(str(c))
        result_str = " ".join(result)
        with open(fname, mode='w') as f:
            f.write(result_str)
            
    encryption(data_dir + a[0])




if __name__ == "__main__":
    pr1()
    pr2()
    pr3()
    pr4()