#!/usr/bin/python3
def print_sorted_dictionary(dic):
    print('\n'.join(['{}: {}'.format(l, v) for l, v in sorted(dic.items())]))
