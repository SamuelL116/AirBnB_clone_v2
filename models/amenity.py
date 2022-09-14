#!/usr/bin/python3
"""module amenity class"""
import sqlalchemy
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
