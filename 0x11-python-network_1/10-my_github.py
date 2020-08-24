#!/usr/bin/python3
""" Hmm """
import requests
from sys import argv

if __name__ == '__main__':
    a = (argv[1], argv[2])
    r = requests.get('https://api.github.com/user', auth=a)
    print(r.json().get('id'))
