#!/usr/bin/python3
"""defines save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
