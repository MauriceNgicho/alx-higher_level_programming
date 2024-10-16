#!/usr/bin/python3
"""
This module defines a script that all arguments to a python list
and save them to a file
"""
import sys
from os.path import exists
"""Iport sys and os"""
# Import functions save_to_json_file and load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# File name to store the JSON data
filename = "add_item.json"

# Load the list from the file if it exists, otherwise start with an empty list
if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add all command-line arguments (excluding the script name) to the list
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)
