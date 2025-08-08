#!/usr/bin/python3
def max_integer(my_list=[]):
    result = 0
    if my_list == []:
        return None
    for i in range(len(my_list) - 1):
        if my_list[i] == my_list[len(my_list) - 1]:
            if result > my_list[i]:
                break
            else:
                result = my_list[i]
                break
        if my_list[i] > my_list[i + 1] and my_list[i] > result:
            result = my_lsit[i]
        elif my_list[i + 1] > my_list[i] and my_list[i + 1] > result:
            result = my_list[i + 1]
        elif result > my_list[i + 1] and result > my_list[i]:
            result = result
    return result
