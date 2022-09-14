#!/usr/bin/python3
"""This is the base model class for AirBnB"""
<<<<<<< HEAD
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, DateTime, Column
import models

=======
import models
import sqlalchemy
import uuid
from datetime import datetime
from sqlalchemy import String, Integer, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os
>>>>>>> d0da4476a5a69766425bf4944a1fde154947caae

Base = declarative_base()


class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """
<<<<<<< HEAD

    id = Column(String(60), unique=True, nullable=False,
                primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
=======
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(),
                        nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(),
                        nullable=False)
>>>>>>> d0da4476a5a69766425bf4944a1fde154947caae

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
<<<<<<< HEAD
=======
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

>>>>>>> d0da4476a5a69766425bf4944a1fde154947caae
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
<<<<<<< HEAD
            if "id" not in kwargs.keys():
                setattr(self, "id", str(uuid.uuid4()))
            time = datetime.now()
            if "created_at" not in kwargs.keys():
                setattr(self, "created_at", time)
            if "updated_at" not in kwargs.keys():
                setattr(self, "updated_at", time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
=======
>>>>>>> d0da4476a5a69766425bf4944a1fde154947caae

    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
<<<<<<< HEAD
        dic = self.to_dict()
        # del dic['__class__']
        # dic['created_at'] = datetime.strptime(dic['created_at'],
        #                                       "%Y-%m-%dT%H:%M:%S")
        # dic['updated_at'] = datetime.strptime(dic['updated_at'],
        #                                       "%Y-%m-%dT%H:%M:%S")
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, dic)
=======
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
>>>>>>> d0da4476a5a69766425bf4944a1fde154947caae

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
<<<<<<< HEAD
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        if '_sa_instance_state' in my_dict.keys():
            my_dict.pop('_sa_instance_state', None)
        return my_dict

    def delete(self):
        """Delete the current instance from the storage
        (models.storage) by calling the method delete"""
=======
        """creates dictionary of the class and returns
        Return:
            returns all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict.pop('_sa_instance_state', None)

        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def delete(self):
        """Deletes current instance"""
>>>>>>> d0da4476a5a69766425bf4944a1fde154947caae
        models.storage.delete(self)
