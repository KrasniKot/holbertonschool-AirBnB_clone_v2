#!/usr/bin/python3
"""This module contains the class DBStorage"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from os import environ, getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """Defines a DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes an DBStorage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB'),
                                             pool_pre_ping=True))
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary"""

        objs = {}
        classes = [State, City, User, Place, Review, Amenity]

        if cls is None:
            for cls in classes:
                objects = self.__session.query(cls).all()
                for obj in objects:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objs[key] = obj
        elif cls in classes:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = f"{obj.__class__.__name__}.{obj.id}"
                objs[key] = obj
        return objs

    def new(self, obj):
        """Adds an object to the current session"""
        self.__session.add(obj)

    def save(self):
        """Commits all the changes on the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes objects from session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads all the data from self.__engine"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                 expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Ends the current session
        """
        self.__session.close()
