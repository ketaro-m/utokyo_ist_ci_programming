import numpy as np
import matplotlib.pyplot as plt
import math


""" return a list of common divisors of two given integers """
def common_divisors(a: int, b: int):
    result = [1]
    gcd = math.gcd(a, b)
    return divisors(gcd)


""" return a list of divisors of a given integer """
def divisors(a: int):
    divs = [1]
    for i in range(2, int(math.sqrt(a))+1):
        if (a % i == 0):
            divs.append(i)
            if not (a == i * i):
                divs.append(int(a / i))
    divs.append(a)
    divs.sort()
    return divs





if __name__ == "__main__":
    print()