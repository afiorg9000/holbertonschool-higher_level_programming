#!/usr/bin/python3
"""Contains the "class_to_json" function"""


import json


def class_to_json(obj):
    """Returns dictionary description"""
    return obj.__dict__
