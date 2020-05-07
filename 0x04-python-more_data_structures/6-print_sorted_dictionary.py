#!/usr/bin/python3
def print_sorted_dictionary(d):
    if d:
        print('\n'.join(['{}: {}'.format(l, v) for l, v in sorted(d.items())]))
