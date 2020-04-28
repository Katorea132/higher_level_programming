#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of", number, end='')
if number < 0:
    print(" is", number % -10, "and is", end='')
    if number % -10 == 0:
        print(" 0")
    else:
        print(" less than 6 and not 0")
else:
    print(" is", number % 10, "and is", end='')
    if number % 10 > 5:
        print(" greater than 5")
    elif number % 10 == 0:
        print(" 0")
    else:
        print(" less than 6 and not 0")
