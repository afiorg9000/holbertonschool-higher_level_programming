#!/usr/bin/python3
"""search API"""
import requests
import sys


if __name__ == "__main__":
    try:
        data = {"q": ""}

    except:
        data = {"q": sys.argv[1]}

    try:
        url = requests.post("http://0.0.0.0:5000/search_user", data)
        if url.json():
            print("[{}] {}".format(url.json().get("id"),
                                   url.json().get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
