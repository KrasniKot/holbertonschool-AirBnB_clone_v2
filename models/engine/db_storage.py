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
        my_dict = {}
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

        if cls:
            if isinstance(cls, str):
                data = self.__session.query(eval(cls)).all()
            else:
                data = self.__session.query(cls).all()
            for obj in data:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                my_dict[key] = obj
        else:
            data = self.__session.query(State).all()
            data += self.__session.query(City).all()
            data += self.__session.query(User).all()
            data += self.__session.query(Place).all()
            data += self.__session.query(Review).all()
            data += self.__session.query(Amenity).all()
            for obj in data:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                my_dict[key] = obj
        return my_dict

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
