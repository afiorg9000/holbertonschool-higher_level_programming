#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file."""
    with open(filename, "a") as f:
        return f.write(text)
