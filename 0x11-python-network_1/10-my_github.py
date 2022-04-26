#!/usr/bin/python3
"""My GitHub!"""

import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    request = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print('{}'.format(request.json().get('id')))
