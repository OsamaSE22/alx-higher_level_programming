#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        size = 0
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end='')
                size += 1
            else:
                continue
        print("")
        return size
    except (TypeError, ValueError):
        return size
