#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a letter"""
import requests
import sys


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        response = r.json()
        if response:
            print(f"[{response.get('id')}] {response.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
