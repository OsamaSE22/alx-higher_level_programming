#!/usr/bin/python3
'''the module contains a funciton that appends content to txt file
and create it if it doesn't exsit'''


def append_write(filename="", text=""):
    '''the function takes the filename and text an append it '''
    with open(filename, 'a', encoding='utf-8') as f:
        result = f.write(text)
    return result
