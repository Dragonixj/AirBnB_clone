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
            *args: list of arguments
            **kwargs: dict of key-values arguments
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key == "upadated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                else:
                    self.__dict__[key] = kwargs[key]
        else:
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
        pass
