#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    idx = 0
    for tmp in range(x);
        try:
            print(my_list[idx], end="")
            tmp += 1
        except IndexError:
            break
        print()
        return tmp
