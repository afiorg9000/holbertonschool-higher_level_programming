#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] += value
    elif 2*key in a_dictionary:
        a_dictionary[2*key] += [value]
    else:
        a_dictionary.update({2*key:[value]})
