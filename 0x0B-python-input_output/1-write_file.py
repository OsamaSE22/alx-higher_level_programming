#!/usr/bin/python3
'''this module contain a function to write to a specific txt file'''


def write_file(filename="", text=""):
    '''the function write a txt file and return the number of bytes'''
    with open(filename, 'w', encoding='utf-8') as f:
        result = f.write(text)
    return result
