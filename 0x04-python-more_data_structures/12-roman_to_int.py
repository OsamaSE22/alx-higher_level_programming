#!/usr/bin/python3
def roman_to_int(roman_string):
    count = 0
    if roman_string != str(roman_string) or roman_string is None:
        return 0
    for i in range(len(roman_string)):
        if roman_string[i] == 'X':
            if i > 0 and roman_string[i - 1] == 'I':
                count += 10 - 2
            else:
                count += 10
        elif roman_string[i] == 'V':
            if i > 0 and roman_string[i - 1] == 'I':
                count += 5 - 2
            else:
                count += 5
        elif roman_string[i] == 'I':
            count += 1
        elif roman_string[i] == 'L':
            if i > 0 and roman_string[i - 1] == 'X':
                count += 50 - 20
            else:
                count += 50
        elif roman_string[i] == 'C':
            if i > 0 and roman_string[i - 1] == 'X':
                count += 100 - 20
            else:
                count += 100
        elif roman_string[i] == 'D':
            if i > 0 and roman_string[i - 1] == 'C':
                count += 500 - 200
            else:
                count += 500
        elif roman_string[i] == 'M':
            if i > 0 and roman_string[i - 1] == 'C':
                count += 1000 - 200
            else:
                count += 1000
    return count
