#!/usr/bin/python3
"""POST an email #"""
import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print("{}".format(r.text))
