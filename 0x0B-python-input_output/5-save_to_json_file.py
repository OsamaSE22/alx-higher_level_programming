#!/usr/bin/python3
'''write python objects to json file'''
import json


def save_to_json_file(my_obj, filename):
    '''pass the python object and filename and
    get the json representation into that file'''
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
