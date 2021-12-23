#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    count = 0
    if length == 0:
        print(0)
    else:
        for i in range(1, length):
            count += int(sys.argv[i])
            print(count)
