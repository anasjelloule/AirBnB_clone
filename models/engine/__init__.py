#!/usr/bin/python3
"""Impliment the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted class storage engine.

    Attributes:
        __file_path (str): name_of_file to save objects to.
        __objects (dict): dictionary_of_instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects obj with key <obj_class_name>.id"""
        anas_oc_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(anas_oc_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path ."""
        anas_o_dict = FileStorage.__objects
        obj_dict = {obj: anas_o_dict[obj].to_dict() for obj in anas_o_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it's exists"""
        try:
            with open(FileStorage.__file_path) as f:
                anas_obj_dict = json.load(f)
                for oq in anas_obj_dict.values():
                    anas_cls_name = oq["__class__"]
                    del oq["__class__"]
                    self.new(eval(anas_cls_name)(**oq))
        except FileNotFoundError:
            return
