#!/usr/bin/python3
def uppercase(s):
    npr = ""
    for i in s:
        if ord(i) >= 97 and ord(i) <= 122:
            nchar = ord(i) - 32
            npr += chr(nchar)
        else:
            npr += i
    print("{}".format(npr))
