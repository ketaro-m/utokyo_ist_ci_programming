import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import copy
import collections 
import utils


data_dir = os.path.join(os.path.dirname(__file__), 'data/')


def ans1(num: int, answering=True):
    num_str = str(num)
    num_str_rv = list(reversed(num_str))
    ans_num = 0
    for i in range(len(num_str_rv)):
        ans_num += int(num_str_rv[i]) * (4 ** i)

    if answering:
        print("No.1 Answer: {} (4) -> {} (10)".format(num, ans_num))
    return ans_num


def ans2(input_num: str, answering=True):
    ans_num = 0
    input_num_rv = list(reversed(input_num))
    for i in range(len(input_num_rv)):
        n = utils.octo_alphabet.index(input_num_rv[i]) # way1
        n = ord(input_num_rv[i]) - 97 # way2
        ans_num += n * (8 ** i)

    if answering:
        print("No.2 Answer: {} -> {} (10)".format(input_num, ans_num))
    return


def ans3():
    input_num = 2015
    # ans_roman = ans5(2015, answering=False)
    ans_roman = 'MMXV'
    print("No.3 Answer: {} -> {}".format(input_num, ans_roman))
    return



def ans4(input_num : str, answering=True):
    ans_num = 0
    for i in range(len(input_num) - 1):
        num = utils.roman_num[input_num[i]]
        next_num = utils.roman_num[input_num[i+1]]
        # case of subtraction
        if num < next_num:
            ans_num -= num
        else:
            ans_num += num
    ans_num += utils.roman_num[input_num[-1]]

    if answering:
        print("No.4 Answer: {} -> {}".format(input_num, ans_num))
    return ans_num

def check_ans4():
    assert ans4('MMXV', answering=False) == 2015
    assert ans4('XIII', answering=False) == 13
    assert ans4('MCMIV', answering=False) == 1904


def ans5(num: int, answering=True):
    num2 = num
    ln = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_num2 = copy.deepcopy(utils.roman_num)
    roman_num2['CM'] = 900
    roman_num2['CD'] = 400
    roman_num2['XC'] = 90
    roman_num2['XL'] = 40
    roman_num2['IX'] = 9
    roman_num2['IV'] = 4
    roman_num2 = collections.OrderedDict(
        sorted(roman_num2.items(), key=lambda x: x[1], reverse=True)
    )
    # --------------------
    # # non-recursive way
    # ans_num = ''
    # index = 0
    # while (num > 0):
    #     if num >= ln[index]:
    #         num -= ln[index]
    #         ans_num += utils.get_key_from_value(roman_num2, ln[index])
    #     else:
    #         index += 1
    # --------------------

    # --------------------
    # recursive-way
    def num2roman(num, ln):
        if num <= 0:
            return ''
        if num >= ln[0]:
            return utils.get_key_from_value(roman_num2, ln[0]) + num2roman(num-ln[0], ln)
        else:
            return num2roman(num, ln[1:])
    ans_num = num2roman(num, ln)
    # --------------------

    if answering:
        print("No.5 Answer: {} -> {}".format(num2, ans_num))
    return ans_num

def check_ans5():
    assert ans5(2015, answering=False) == 'MMXV'
    assert ans5(13, answering=False) == 'XIII'
    assert ans5(1904, answering=False) == 'MCMIV'


def ans6(num, answering=True):
    num2 = num
    numbers = list(utils.roman_num.values())

    # --------------------
    # recursive-way
    def num2roman(num, ln):
        if num <= 0:
            return ''
        if num >= ln[0]:
            return utils.get_key_from_value(utils.roman_num, ln[0]) + num2roman(num-ln[0], ln)
        else:
            sub_version_txt = ' '*1000
            for i in reversed(range(1, len(ln))):
                possible_num = ln[0] - ln[i]
                if num >= possible_num:
                    sub_version_txt = ''
                    sub_version_txt += utils.get_key_from_value(utils.roman_num, ln[i])
                    sub_version_txt += utils.get_key_from_value(utils.roman_num, ln[0])
                    sub_version_txt += num2roman(num-(ln[0]-ln[i]), ln)
                    break
            return min(num2roman(num, ln[1:]), sub_version_txt, key=len) # compare
    ans_num = num2roman(num, numbers)
    # --------------------

    if answering:
        print("No.6 Answer: {} -> {}".format(num2, ans_num))
    return ans_num


def check_ans6():
    assert ans6(2015, answering=False) == 'MMXV'
    assert ans6(13, answering=False) == 'XIII'
    assert ans6(1904, answering=False) == 'MCMIV'
    assert ans6(149, answering=False) == 'CIL'
    assert ans6(49, answering=False) == 'IL'


def ans7(text :str, answering=True):
    text_list = text.split()
    ans_num = 0
    buf = 0
    for t in text_list:
        if t == 'thousand':
            ans_num += (buf * 1000)
            buf = 0
        elif t == 'hundred':
            ans_num += (buf * 100)
            buf = 0
        else:
            buf += utils.alphabet_num.get(t)
    ans_num += buf
    if answering:
        print("No.7 Answer: {} -> {}".format(text, ans_num))
    return ans_num


def check_ans7():
    assert ans7('fifty four thousand three hundred twelve', answering=False) == 54312
    assert ans7('one thousand two hundred', answering=False) == 1200
    assert ans7('twelve hundred', answering=False) == 1200


def main():
    ans1(123)
    ans2('bcd')
    ans3()
    ans4('IIV')
    check_ans4()
    ans5(2015)
    check_ans5()
    ans6(149)
    check_ans6()
    ans7('fifty four thousand three hundred twelve')
    check_ans7()
    return



if __name__ == "__main__":
    main()