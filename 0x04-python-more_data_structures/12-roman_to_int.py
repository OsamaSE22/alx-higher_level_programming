#!/usr/bin/python3
def roman_to_int(roman_string):
    count = 0
    for i in roman_string:
        if i == 'X':
            count += 10
        elif i == 'V':
            count += 5
        elif i == 'I':
            count += 1
        elif i == 'L':
            count += 50
        elif i == 'C':
            count += 100
        elif i == 'D':
            count += 500
        elif i == 'M':
            count += 1000
    return count
