#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        print(sorted(self))
