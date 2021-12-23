#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = 0
    for idx in range(len(sys.argv) - 1):
        count += int(sys.argv[idx + 1])
    print("{}".format(count))
