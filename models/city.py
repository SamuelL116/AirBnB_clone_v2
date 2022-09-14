#!/usr/bin/python3
<<<<<<< HEAD
"""This is the city class"""
from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
=======
"""module for city class"""
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
>>>>>>> d0da4476a5a69766425bf4944a1fde154947caae


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
<<<<<<< HEAD
        state_id: The state id
        name: input name
=======
        state_id: column for state id (foreign key)
        name: column for name of city
        __tablename__: name of table in MySQL
>>>>>>> d0da4476a5a69766425bf4944a1fde154947caae
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
<<<<<<< HEAD
    places = relationship('Place', backref='cities',
                          cascade='all, delete-orphan')
=======
    places = relationship("Place", cascade="all, delete", backref="cities")
>>>>>>> d0da4476a5a69766425bf4944a1fde154947caae
