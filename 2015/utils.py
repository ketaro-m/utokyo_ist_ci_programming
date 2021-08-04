import numpy as np
import matplotlib.pyplot as plt
import collections
import main



""" list for problem2 """
octo_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


""" dict of roman number """
roman_num = collections.OrderedDict({'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1})


""" dict of english number """
alphabet_num = collections.OrderedDict({
    'thousand':1000, 'hundred':500, 'ninety':90, 'eighty':80, 'seventy':70, 'sixty':60, 'fifty':50, 'forty':40, 'thirty':30, 'twenty':20,
    'nineteen':19, 'eighteen':18, 'seventeen':17, 'sixteen':16, 'fifteen':15, 'fourteen':14, 'thirteen':13, 'twelve':12, 'eleven':11,
    'ten':10, 'nine':9, 'eight':8, 'seven':7, 'six':6, 'five':5, 'four':4, 'three':3, 'two':2, 'one':1})


""" return a key of val in d (dictionary) """
def get_key_from_value(d, val):
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return None



if __name__ == "__main__":
    print()