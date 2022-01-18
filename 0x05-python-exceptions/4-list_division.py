#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = []
    for idx in range(list_length):
        try:
            count.append(my_list_1[idx]/my_list_2[idx])
        except TypeError:
            print("wrong type")
            count.append(0)
        except ZeroDivisionError:
            print("division by 0")
            count.append(0)
        except IndexError:
            print("out of range")
            count.append(0)
        finally:
            continue

    return count
