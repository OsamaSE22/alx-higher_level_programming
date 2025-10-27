#!/usr/bin/python3
'''this is a script that get command line arguments and
add it to a json file '''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
try:
    readfile = load_from_json_file("add_item.json")
    for i in my_list:
        readfile.append(i)
    save_to_json_file(readfile, "add_item.json")
except Exception:
    save_to_json_file(my_list, "add_item.json")
