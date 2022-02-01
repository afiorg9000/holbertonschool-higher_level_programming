#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r') as f:
        text = f.readlines()

    with open(filename, 'w') as f:
        for line in text:
            if search_string in line:
                line +=new_string
            f.write(line)
