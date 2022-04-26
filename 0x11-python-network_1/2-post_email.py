#!/usr/bin/python3
""" POST an email #0 """
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    requests = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(requests) as response:
        print(response.read().decode('ascii'))
