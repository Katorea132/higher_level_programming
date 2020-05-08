#!/bin/usr/python3
def weight_average(my=[]):
    if my:
        return sum(tuple(n1 * n2 for n1, n2 in my))/sum(num[1] for num in my)
    return 0
