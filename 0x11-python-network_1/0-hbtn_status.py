#!/usr/bin/python3
# Requests with urllib
from urllib import request

if __name__ == '__main__':
    with request.urlopen('htts://intranet.hbtn.io/status') as r:
        r = r.read()
        print('Body response:')
        print('\t- type: {}\n\t- content: {}\n\t- \
    utf8 content: {}'.format(type(r), r, r.decode('utf-8')))
