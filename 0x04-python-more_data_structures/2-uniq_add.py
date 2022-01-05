#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []

    for i in range(len(my_list)):
        if my_list[i] not in new_list:
            new_list.append(my_list[i])
    return sum(new_list)
