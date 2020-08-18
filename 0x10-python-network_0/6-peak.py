#!/usr/bin/python3
"""FInds peaks
"""

def find_peak(lili):
    if lili:
        return sorted(lili)[-1]
    return None
