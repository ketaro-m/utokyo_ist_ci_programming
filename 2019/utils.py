import numpy as np

""" return True if all the elements of two given lists are the same
usage : assert compare_lists(actual, expected) """
def compare_lists(actual, expected):
    return all([a == b for a, b in zip(actual, expected)])


def binary2code(binary):
    num = int(binary, 2)
    assert num < 2**6
    if num < 26:
        return chr(num + 65)
    elif num < 26*2:
        return chr(num - 26 + 97)
    elif num < 26*2+10:
        return chr(num - 26*2 + 48)
    elif num == 26*2+10:
        return "@"
    else:
        return "#"


def code2binary(code):
    num = 0
    ascii_num = ord(code)
    if code == "#":
        num = 2**6-1
    elif code == "@":
        num = 2**6-2
    elif ascii_num < 58:
        num = ascii_num - 48 + 26*2
    elif ascii_num < 91:
        num = ascii_num - 65
    else:
        num = ascii_num - 97 + 26
    return format(num, 'b')



def test_coding():
    text = ""
    for i in range(2**6):
        # print(format(i, 'b'))
        text += binary2code(format(i, 'b'))
    print(text)

    num_ln = []
    index = 0
    for i in text:
        num_ln.append(code2binary(i))
        print(num_ln[index], index, i)
        assert int(num_ln[index], 2) == index
        index += 1
    print(num_ln)


def readBinary(fname):
    with open(fname, mode='rb') as f:
        s = f.read()
    # print(len(s), s)
    result = []
    for b in s:
        # print(hex(b))
        result.append(hex(b))
    # print(result)
    return result


def compareBinaryFiles(f1,f2):
    return compare_lists(readBinary(f1), readBinary(f2))


def compareTextFiles(f1, f2):
    with open(f1, mode='r') as f:
        s1 = f.read()
    with open(f2, mode='r') as f:
        s2 = f.read()
    return s1 == s2


# return 0~28, a=0, z=25, period=26, space=27
def alphabet2num(alphabet):
    asci = ord(alphabet)
    if asci == 32:
        return 27
    elif asci == 46:
        return 26
    else:
        num = asci - 97
        # assert num >=0 and num < 26
        return num

def num2alphabet(num):
    assert num >= 0 and num < 28, "number must be from 0 to 27"
    if num == 27:
        return ' '
    elif num == 26:
        return '.'   
    else:
        return chr(num + 97)

""" print out decode_map for debugging for problem4 """
def print_decode_map(decode_map):
    assert len(decode_map) == 28, "invalid input"
    known_num = sum([1 if i != -1 else 0 for i in decode_map])
    print("Decode Map {}/28".format(known_num))
    print("--------------")
    for i in range(len(decode_map)):
        if decode_map[i] == -1:
            print("{} -> *".format(num2alphabet(i)))
        else:
            print("{} -> {}".format(num2alphabet(i), num2alphabet(decode_map[i])))
    print("--------------")


""" return True if given two srting has no match character
"abcd" and "ecfg" -> False
"abcd" and "efgh" -> True """
def no_match(s1: str, s2: str):
    assert len(s1) == len(s2), "two strings must be the same length"
    for i in len(s1):
        if s1[i] == s2[i]:
            return False
    return True

""" return how many characters are matched in two given strings """
def match_num(s1: str, s2: str):
    assert len(s1) == len(s2), "two strings must be the same length"
    counter = 0
    for i in len(s1):
        if s1[i] == s2[i]:
            counter += 1
    return counter



def PrimeFactorization(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


if __name__ == "__main__":
    test_coding()