#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    liso = list(a_dictionary.items())
    liso.sort()
    liso = dict(liso)
    for i, j in liso.items():
        print("{0}: {1}".format(i, j))
