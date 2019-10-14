# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def smallMult():
    found = False
    i = 2520

    while not found:
        flag = True
        for j in range(11, 20+1):
            if i % j != 0:
                flag = False
                break
        if flag:
            found = True
            return i
        i += 1


print(smallMult())

"""" Best option

from math import gcd
from functools import reduce

#def lcm(a,b):
  return a*b//gcd(a,b)

print(reduce(lcm, range(11,20+1)))
"""
