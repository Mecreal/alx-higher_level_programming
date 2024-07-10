#!/usr/bin/python3
"""Uses the GitHub API to display your id"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, token))
    print(r.json().get('id'))
