#!/usr/bin/python3
"Response header value"
import requests
from sys import argv
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
