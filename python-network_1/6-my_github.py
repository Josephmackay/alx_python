#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))

    try:
        data = response.json()
        print(data.get('id', 'None'))
    except ValueError:
        print('None')
