#!/usr/bin/python3
""" Hmm """
import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get('https://api.github.com/repos/\
{}/{}/commits'.format(argv[1], argv[2]))
    counter = 0
    for j in r.json():
        if counter > 9:
            break
        print('{}: {}'.format(j['sha'], j['commit']['author']['name']))
        counter += 1
