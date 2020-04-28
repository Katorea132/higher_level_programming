#!/usr/bin/python3
for a in range(ord('z'), ord('a') - 1, -1):
    if a % 2 == 1:
        a -= 32
    print('{:c}'.format(a), end='')
