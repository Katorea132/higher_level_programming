#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    count = 0
    for num in sys.argv[1:]:
        count += int(num)
    print(count)
