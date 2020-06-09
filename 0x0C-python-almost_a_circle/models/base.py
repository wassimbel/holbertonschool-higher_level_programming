#!/usr/bin/python3
""" module - class Base """
import json


class Base:
    """  This class will be the “base” of all other classes in this project.
        The goal of it is to manage id attribute in all your future classes
        and to avoid duplicating the same code (by extension, same bugs) """
    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiates id, if id is not none assign value
            else increment and assign  """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        mylist = []
        with open(cls.__name__ + ".json", mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write(Base.to_json_string(mylist))
            else:
                for i in list_objs:
                    mylist.append(cls.to_dictionary(i))
                file.write(Base.to_json_string(mylist))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)

        else:
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

