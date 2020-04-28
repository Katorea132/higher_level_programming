#!/usr/bin/python3
def uppercase(str):
    for l in str:
        if ord(l) >= ord('a') and ord(l) <= ord('z'):
            l = chr(ord(l) - 32)
        print('{:c}'.format(l), end='')
    print('')
