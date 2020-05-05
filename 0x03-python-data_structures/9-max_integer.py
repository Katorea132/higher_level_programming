#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = 0
        for n in my_list:
            if max < n:
                max = n
        return max
    return None
