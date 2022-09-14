#!/usr/bin/python3
<<<<<<< HEAD
"""create a unique FileStorage instance for your application"""
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
=======
"""Unique FileStorage instance for your application"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os

if 'HBNB_TYPE_STORAGE' in os.environ\
        and os.environ['HBNB_TYPE_STORAGE'] == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
>>>>>>> d0da4476a5a69766425bf4944a1fde154947caae
