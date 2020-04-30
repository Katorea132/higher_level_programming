#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("""{0} + {1} = {2}
{0} - {1} = {3}
{0} * {1} = {4}
{0} / {1} = {5}
""".format(a, b, add(a, b), sub(a, b), mul(a, b), div(a, b)), end='')
