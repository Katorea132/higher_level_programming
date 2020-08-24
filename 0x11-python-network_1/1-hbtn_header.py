#!/usr/bin/python3
# More urllib
from urllib import request
import sys

if __name__ == '__main__':
    with request.urlopen(sys.argv[1]) as r:
        print(r.getheader('X-Request-Id'))
