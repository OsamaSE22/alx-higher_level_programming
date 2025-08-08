#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for element in range(0, (len(new_list) - 1)):
        if (new_list[element] % 2 == 0):
            new_list[element] = True
        else:
            new_list[element] = False
    return new_list
