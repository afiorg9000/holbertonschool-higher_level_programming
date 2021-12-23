#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    length = len(argv) -1

    if length == 0:
        print("{:d} arguments.".format(length))
    elif length == 1:
        print("{:d} argument:".format(length))
        print("{:d}: {}".format(length, argv[1]))
    else:
        print("{:d} arguments:".format(length))
        for number in range(1, length + 1):
                print("{:d}: {}".format(number, argv[number]))
