#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{0:d} {1:s}".format(len(argv) - 1, "arguments."))
    elif len(argv) == 2:
        print("{0:d} {1:s}".format(len(argv) - 1, "argument:"))
        print("1: {0:s}".format(argv[1]))
    else:
        print("{0:d} {1:s}".format(len(argv) - 1, "arguments:"))
        for i in range(1, len(argv)):
            print("{0:d}: {1:s}".format(i, argv[i]))
