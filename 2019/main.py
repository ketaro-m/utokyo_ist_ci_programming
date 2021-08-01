import numpy as np
import pandas as pd
import copy
import collections
import utils
import time
import itertools


def fn1(path):
    with open(path) as f:
        s = f.read()
        print(len(s))

    binaries = ""
    for code in s:
        binaries += utils.code2binary(code)
    print(len(binaries))
    print(binaries[310:321])


def fn2(path):
    with open(path, mode='rb') as f:
        s = f.read()
    result = []
    skip = 0
    for i in range(len(s)):
        if skip:
            skip -= 1
            continue
        if s[i] > 0:
            result.append(s[i])
        else:
            start = i - s[i + 1]
            end = start + s[i + 2]
            result.extend(s[start:end])
            skip = 2
    print(len(result))
    barray = bytearray(result)
    with open(path.replace('.bin', '.txt'), mode='wb') as f:
            f.write(barray)


def fn3(path):
    with open(path, mode='rb') as f:
        s = f.read()
    result = []
    reservation = [False, [0, [0, 0]]] # [flag, [i, [j, match_len]]]
    for i in range(len(s)):
        max_match_len = [0, 0] # [index of j, length]
        for j in range(i):
            match_len = 0
            while (s[j + match_len] == s[i + match_len]):
                match_len += 1
                if (i + match_len >= len(s)) or (j + match_len >= i):
                    break
            # update
            if match_len > max_match_len[1]:
                max_match_len[0] = j
                max_match_len[1] = match_len

        if reservation[0]:
            if (i >= reservation[1][0] + reservation[1][1][1]):
                # execute compression
                reservation[0] = False
                p = reservation[1][0] - reservation[1][1][0]
                d = reservation[1][1][1]
                result.extend([0x00, p, d])
            else:
                if (max_match_len[1] <= reservation[1][1][1]):
                    pass
                else:
                    # update reservation
                    result.extend(s[reservation[1][0]:i])
                    reservation[1] = [i, max_match_len]
        
        if not reservation[0]:
            if (max_match_len[1] <= 3):
                # no need to compress
                result.append(s[i])
            else:
                reservation[0] = True
                reservation[1] = [i, max_match_len]

    # print(len(result))
    barray = bytearray(result)
    with open(path.replace('.txt', '.bin').replace('.png', '.bin'), mode='wb') as f:
            f.write(barray)

    # test result
    print(path, utils.compareBinaryFiles(path.replace('.txt', '.bin').replace('.png', '.bin'), path.replace('.txt', '_ans.bin').replace('.png', '_ans.bin')))


# if search all patterns, 28! patterns are needed: impossible
# first search for which one is converted to space.
def fn4(fname: str):
    dict_fname = fname.replace('.txt', '_dict.txt')
    with open(fname, mode='r') as f:
        enc_str = f.read()
    with open(dict_fname, mode='r') as f:
        dict_str = f.read()
    
    dict_ln = dict_str.split()
    dict_ln.sort(key=len)
    decode_map = [-1]*28 # a~z, period, space,
    # search for which one is converted to space and period
    sp_possible = [] # a list of pair(list) for possible space and period index
    words_len = [len(w) for w in dict_ln]
    for i in range(len(decode_map)):
        for j in range(len(decode_map)):
            if (j == i): continue
            # i:space, j:period
            char_from_space = utils.num2alphabet(i)
            char_from_period = utils.num2alphabet(j)
            # print((char_from_space, char_from_period))
            enc_str2 = enc_str.replace(' ', 'S') # temporary replace space with S
            enc_str2 = enc_str2.replace(char_from_space, ' ')
            enc_str2 = enc_str2.replace('.', 'P') # temporary replace period with P
            enc_str2 = enc_str2.replace(char_from_period, '.')
            enc_str2 = enc_str2.replace('.', '')

            enc_str2_ln = enc_str2.split()
            enc_str2_ln = list(dict.fromkeys(enc_str2_ln))
            for wi in range(len(enc_str2_ln)): enc_str2_ln[wi] = enc_str2_ln[wi].replace('P', '.').replace('S', ' ') # return to original
            # print(enc_str2_ln[0])
            enc_str2_ln.sort(key=len)
            enc_str2_ln_len = [len(w) for w in enc_str2_ln]
            if utils.compare_lists(words_len, enc_str2_ln_len):
                sp_possible.append([i, j])
                enc_dict_ln = enc_str2_ln
    
    
    if len(sp_possible) == 1:
        print("Space and Period are detected!")
        print('space: {}, period: {}'.format(utils.num2alphabet(sp_possible[0][0]), utils.num2alphabet(sp_possible[0][1])))
    else:
        for sp in sp_possible:
            print('Possible space and period')
            print(' space: {}, period: {}'.format(utils.num2alphabet(sp[0]), utils.num2alphabet(sp[1])))
    print("----------------------------------------------------\n\n\n")


    for sp in sp_possible:
        decode_map[sp[0]] = utils.alphabet2num(' ')
        decode_map[sp[1]] = utils.alphabet2num('.')
        dict_ln_2d = []
        enc_dict_ln_2d = []
        od = collections.OrderedDict(collections.Counter(words_len))
        # od = collections.OrderedDict(
        #     sorted(od.items(), key=lambda x: x[1], reverse=False)
        # )
        print(od)
        # create a list of lists of the same length words
        counter = 0
        for i,v in od.items():
            dict_ln_2d.append(dict_ln[counter:counter+v])
            enc_dict_ln_2d.append(sorted(enc_dict_ln[counter:counter+v]))
            counter += v
        # dict_ln_2d.sort(key=len, reverse=True)
        # enc_dict_ln_2d.sort(key=len, reverse=True)


        def decode(text: str, decode_map: list):
            result = ""
            for w in text:
                w_n = utils.alphabet2num(w)
                if decode_map[w_n] != -1:
                    result += utils.num2alphabet(decode_map[w_n])
                else:
                    result += w
            assert len(text) == len(result)
            return result


        for i in range(len(dict_ln_2d)):
            print()
            print(enc_dict_ln_2d[i])
            print(dict_ln_2d[i])
        # keep updating the decode_map
        update_flag = True
        while (update_flag):
            print("----------------------------------------------------")
            update_flag = False
            for i in range(len(dict_ln_2d)):
                # update decode_map if enc-dec words are 1vs1 pair: the pairs of characters in those two words are finalized
                if (len(enc_dict_ln_2d[i]) == 1):
                    print("decoding: {} -> {}".format(enc_dict_ln_2d[i][0], dict_ln_2d[i][0]))
                    for wi in range(len(enc_dict_ln_2d[i][0])):
                        enc_char = enc_dict_ln_2d[i][0][wi]
                        dec_char = dict_ln_2d[i][0][wi]
                        decode_map[utils.alphabet2num(enc_char)] = utils.alphabet2num(dec_char)
            utils.print_decode_map(decode_map)

            for i in range(len(dict_ln_2d)):
                remove_after = [] # temporary storage
                for enc_word in enc_dict_ln_2d[i]:
                    dec_word = decode(enc_word, decode_map) # decode using decode_map
                    if dec_word in dict_ln_2d[i]:
                        remove_after.append([enc_word, dec_word])
                        update_flag = True
                for v in remove_after:
                    enc_dict_ln_2d[i].remove(v[0])
                    dict_ln_2d[i].remove(v[1])
                # for debugging
                if len(dict_ln_2d[i]) > 0:
                    print()
                    print([decode(w, decode_map) for w in enc_dict_ln_2d[i]])
                    print(dict_ln_2d[i])

            print()
            time.sleep(0.5)



        """ search all patterns at last """
        print("Search all remaining patterns ...")
        unknow_idx = np.array([i for i in range(len(decode_map)) if decode_map[i] == -1])
        unknow_num = np.array([i for i in range(28) if i not in decode_map])
        decode_map_array = np.array(decode_map)
        for v in itertools.permutations(unknow_num, len(unknow_idx)):
            enc_dict_ln_2d_copy = copy.deepcopy(enc_dict_ln_2d)
            dict_ln_2d_copy = copy.deepcopy(dict_ln_2d)
            decode_map_array[unknow_idx] = v
            decode_map_possible = list(decode_map_array)
            for i in range(len(dict_ln_2d_copy)):
                remove_after = [] # temporary storage
                for enc_word in enc_dict_ln_2d_copy[i]:
                    dec_word = decode(enc_word, decode_map_possible) # decode using decode_map
                    if dec_word in dict_ln_2d[i]:
                        remove_after.append([enc_word, dec_word])
                for v in remove_after:
                    enc_dict_ln_2d_copy[i].remove(v[0])
                    dict_ln_2d_copy[i].remove(v[1])

            
            # judge whether this pattern is the answer
            flag = True
            for i in range(len(dict_ln_2d_copy)):
                if len(enc_dict_ln_2d_copy[i]) > 0 or len(dict_ln_2d_copy[i]) > 0:
                    flag = False

            if flag:
                decode_map = decode_map_possible
                dec_str = decode(enc_str, decode_map)
                with open(fname.replace('.txt', '_ans.txt'), mode='r') as f:
                    ans_str = f.read()
                assert ans_str == dec_str

                print("------------------------------------------------")
                print("Decryption succeeded!")
                utils.print_decode_map(decode_map)
                print(enc_str)
                print()
                print("|")
                print("v")
                print()
                print(dec_str)
                return 
                    
    print("Decription failed...")
    return



def fn5():
    e = 551263368336670859257571
    n = 3858843578360632069557337
    print(utils.PrimeFactorization(8))


def main():
    # fn1("data/data1.txt")
    # fn2("data/data2a.bin")
    # fn3("data/data3a.txt")
    # fn3("data/data3b.png")
    fn4("data/data4_jobs.txt")
    # fn5()
    return



if __name__ == "__main__":
    main()