#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(60), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="states")

    @property
    def cities(self):
        """Getter method"""
        from models import storage

        listOfCities = []
        for city in storage.all(City):
            if city.state_id == self.id:
                listOfCities.append(city)
        return listOfCities
