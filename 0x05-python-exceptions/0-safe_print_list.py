#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for tmp in range(x):
        try:
            print("{}".format(my_list[tmp]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return (count)
