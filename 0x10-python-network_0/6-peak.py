#!/usr/bin/python3
"""FInds peaks
"""

def find_peak(lili):
    """COmment
    """
    if lili:
        lili.sort()
        return lili[-1]
    return None
