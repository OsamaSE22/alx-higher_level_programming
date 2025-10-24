#!/usr/bin/python3
'''this module contains a funciton to read txt files'''


def read_file(filename=""):
    '''pass the filename with its path and it will be read
    by this funciton and printed'''
    with open(filename, encoding='utf-8') as f:
        print(f.read())
