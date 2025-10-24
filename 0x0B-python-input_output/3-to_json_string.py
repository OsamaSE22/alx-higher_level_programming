#!/usr/bin/python3
'''this module contains a function that
return a python object to a json string'''


import json
def to_json_string(my_obj):
    '''return a json representation to the python object'''
    return json.dumps(my_obj)
