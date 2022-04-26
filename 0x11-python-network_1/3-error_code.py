#!/usr/bin/python3
""" Error code """

from urllib.error import HTTPError
import urllib.request
from sys import argv
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
