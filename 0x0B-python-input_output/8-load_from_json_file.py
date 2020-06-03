#!/usr/bin/python3
""" module - function load_from_json_file """
import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file """
    with open(filename, encoding="utf-8") as myfile:
        return json.load(myfile)
