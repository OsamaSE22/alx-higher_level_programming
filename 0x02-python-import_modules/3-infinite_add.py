#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = 0
    if len(argv) < 3:
        print("{0:d}".format(a))
    elif len(argv) >= 3:
        for i in range(1, len(argv)):
            a += int(argv[i])
        print(a)
