#!/usr/bin/python3
# more D:
from urllib import request, parse, error
import sys

if __name__ == '__main__':
    try:
        with request.urlopen(sys.argv[1]) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
