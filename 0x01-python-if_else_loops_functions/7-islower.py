#!/usr/bin/python3
def islower(c):
    for low in range(ord('a'), ord('z') + 1):
        if ord(c) == low:
            return True
    else:
        return False
