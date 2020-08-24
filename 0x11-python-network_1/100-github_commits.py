#!/usr/bin/python3
""" Hmm """
import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get('https://api.github.com/repos/\
{}/{}/commits'.format(argv[2], argv[1]))
    counter = 0
    for j in r.json()[:10]:
        print('{}: {}'
              .format(j.get('sha'), j.get('commit').get('author').get('name')))
