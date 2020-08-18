#!/usr/bin/python3
"""FInds peaks
"""

def find_peak(lili):
    if lili:
        if len(lili) > 1:
            if lili[0] > lili[1]:
                return lili[0]
            elif lili[-1] > lili[-2]:
                return lili[-1]
        return sorted(lili)[-1]
    return None
