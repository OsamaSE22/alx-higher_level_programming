#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        liso = list(a_dictionary.values())
        liso = max(liso)
        for i, j in a_dictionary.items():
            if j == liso:
                return i
    else:
        None
