#!/usr/bin/python3
""" module that contains base class """


import json

class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """import dictionary list to json"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
