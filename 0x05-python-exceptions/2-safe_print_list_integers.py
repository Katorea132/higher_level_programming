#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nums = 0
    for numbers in my_list:
        try:
            if nums <= x:
                print('{d}'.format(numbers), end='')
                nums += 1
            except TypeError:
                continue;
            else:
                break;
    print()
    return nums
