#!/usr/bin/python3
# man, requests is the best
import requests
import sys

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    if r.status > 400:
        print('Error code:', r.status_code)
    else:
        print(r.text)
