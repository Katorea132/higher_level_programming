#!/usr/bin/python3
""" naichu """
from sys import argv
import requests

if __name__ == '__main__':
    q = ""
    if len(argv) > 1:
        q = argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        j = r.json()
        if j:
            print("[{}] {}".format(j.get('id'), j.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
