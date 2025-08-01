#!/usr/bin/python3
def uppercase(s):
    for i in s:
        if ord(i) >= 97 and ord(i) <= 122:
            nchar = ord(i) - 32
            print(chr(nchar), end='')
        elif ord(i) >= 65 and ord(i) <= 90:
            print(i, end='')
        else:
            print(i, end='')
    print()
