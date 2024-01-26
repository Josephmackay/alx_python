#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://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@github.com/Josephmackay/alx_python'
    auth = (username, token)
    response = requests.get(url, auth=auth)

    try:
        user_data = response.json()
        print(user_data.get('id', None))
    except ValueError:
        print(None)
