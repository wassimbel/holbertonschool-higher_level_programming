#!/usr/bin/python3
""" module - function save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file,
     using a JSON representation """
    with open(filename, mode="w", encoding="utf-8") as myfile:
        return myfile.write(json.dumps(obj))
