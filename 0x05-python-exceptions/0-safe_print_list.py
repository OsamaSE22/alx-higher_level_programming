#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        size = 0
        xSize = 0
        for k in my_list:
            size += 1
        if (size >= x):
            for i in range(0, x):
                print(my_list[i], end='')
                xSize += 1
            print("")
        else:
            raise IndexError
    except IndexError:
        xSize = 0
        for j in my_list:
            print(j, end='')
            xSize += 1
        print("")
    return xSize
