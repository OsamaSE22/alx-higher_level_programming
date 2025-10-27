#!/usr/bin/python3
'''this module load content from json file
and convert it to a python object'''
import json


def load_from_json_file(filename):
    '''pass a file name
    and get the python object'''
    with open(filename, 'r') as f:
        result = json.load(f)
    return result
