#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    times = 0
    for words in my_list:
        try:
            if words <= x:
                print(words, end='')
                times += 1
            else:
                break
        except:
            break
    print()
    return times
