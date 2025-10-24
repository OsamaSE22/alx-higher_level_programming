#!/usr/bin/python3
'''this module contain a function that return
the string json format to a python object(data structure)'''
import json


def from_json_string(my_str):
    '''pass the json string and get the python object data structure'''
    return json.loads(my_str)
