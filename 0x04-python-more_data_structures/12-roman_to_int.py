#!/usr/bin/python3
def roman_to_int(roman_string):
    val = 0
    if roman_string and type(roman_string) is str and roman_string.isalpha():
        rs = roman_string.upper()
        for i in range(len(rs)):
            if rs[i] is 'I':
                if i + 1 >= len(rs) or rs[i + 1] is 'I':
                    val += 1
                else:
                    val -= 1
            elif rs[i] is 'V':
                val += 5
            elif rs[i] is 'X':
                if i + 1 >= len(rs) or rs[i + 1] in 'IVX':
                    val += 10
                else:
                    val -= 10
            elif rs[i] is 'L':
                val += 50
            elif rs[i] is 'C':
                if i + 1 >= len(rs) or rs[i + 1] in 'IVXLC':
                    val += 100
                else:
                    val -= 100
            elif rs[i] is 'D':
                val += 500
            elif rs[i] is 'M':
                if i + 1 >= len(rs) or rs[i + 1] in 'IVXLCD':
                    val += 1000
                else:
                    val -= 1000
            else:
                return 0
    return val
