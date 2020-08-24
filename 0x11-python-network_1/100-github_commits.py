#!/usr/bin/python3
# Hmm
import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get('https://api.github.com/repos/\
{}/{}/commits'.format(argv[1], argv[2]))
    for j in r.json():
        print('{}: {}'.format(j['sha'], j['commit']['author']['name']))
