#!/usr/bin/python3
# more urllib
from urllib import request, parse
import sys

if __name__ == '__main__':
    pars = parse.urlencode({'email': sys.argv[2]}).encode()
    with request.urlopen(sys.argv[1], pars) as r:
        print(r.read().decode('utf-8'))
