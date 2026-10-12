#!/usr/bin/python3
"""File storage engine for the AirBnB clone."""

import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes them."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all stored objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to storage."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to the JSON file."""
        objects_dict = {}

        for key, obj in self.__objects.items():
            objects_dict[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserialize the JSON file, if it exists."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                objects_dict = json.load(file)

            for key, value in objects_dict.items():
                class_name = value["__class__"]

                if class_name == "BaseModel":
                    from models.base_model import BaseModel
                    self.__objects[key] = BaseModel(**value)

                elif class_name == "User":
                    from models.user import User
                    self.__objects[key] = User(**value)

                elif class_name == "State":
                    from models.state import State
                    self.__objects[key] = State(**value)

                elif class_name == "City":
                    from models.city import City
                    self.__objects[key] = City(**value)

                elif class_name == "Amenity":
                    from models.amenity import Amenity
                    self.__objects[key] = Amenity(**value)

                elif class_name == "Place":
                    from models.place import Place
                    self.__objects[key] = Place(**value)

                elif class_name == "Review":
                    from models.review import Review
                    self.__objects[key] = Review(**value)

        except FileNotFoundError:
            pass