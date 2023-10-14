#!/usr/bin/python3
"""
A module that implements the BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    A class that serves as a base for all common attributes and other classes
    """

    def __init__(self, *args, **kwargs):
        """Initializes the instance attributes

        Args:
            *args: list of arguments(Unused)
            **kwargs: dict that contains attribute values
        """
        if kwargs:
            # Initializes attributes from kwargs
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        setattr(
                            self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        )
                    else:
                        setattr(self, key, value)

        else:
            # Initializes a new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return the string representation
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates self.updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all key/values of __dict__
        of instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
