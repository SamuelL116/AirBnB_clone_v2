#!/usr/bin/python3
<<<<<<< HEAD
"""This is the amenity class"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """This is the class for Amenity
=======
"""module amenity class"""
import sqlalchemy
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class
>>>>>>> d0da4476a5a69766425bf4944a1fde154947caae
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
<<<<<<< HEAD
    if getenv("HBNB_TYPE_STORAGE") == "db":
        place_amenities = relationship('Place',
                                       secondary='place_amenity',
                                       back_populates='amenities')
=======
    place_amenities = relationship("Place", secondary=place_amenity)
>>>>>>> d0da4476a5a69766425bf4944a1fde154947caae
