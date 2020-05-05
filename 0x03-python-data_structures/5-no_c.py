#!/usr/bin/python3
def no_c(my_string):
    return ''.join(str(i) for i in my_string if i is not 'c' and i is not 'C')