#!/usr/bin/python3
import json

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        if type(attrs) is list:
            x = {}
            for i in range(len(attrs)):
                if attrs[i] in self.__dict__:
                    x[attrs[i] = self.__dict__[attrs[i]]

            return x

        else:
        return self.__dict__



