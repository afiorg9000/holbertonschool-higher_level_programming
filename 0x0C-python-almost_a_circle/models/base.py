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
        """Return the JSON serialization of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """"writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            jsonfile.write("[]")
        else:
            jsonfile.write(Base.to_json_string)
