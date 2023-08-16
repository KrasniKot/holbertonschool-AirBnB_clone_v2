#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
from models.review import Review
from models.user import User


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    place_amenity = Table("place_amenity", Base.metadata, Column(
            "place_id",
            String(60),
            ForeignKey("places.id"),
            primary_key=True,
            nullable=False), Column(
                        "amenity_id",
                        String(60),
                        ForeignKey("amenities.id"),
                        primary_key=True,
                        nullable=False))

    if getenv("HBNB_TYPE_STORAGE") == "db":

        amenities = relationship(
                        "Amenity",
                        secondary="place_amenity",
                        viewonly=False)

        reviews = relationship('Review', cascade='all, delete',
                               backref='place')

    else:

        @property
        def reviews(self):
            """ Return revlist """
            from models import storage
            revlist = []
            for review in self.reivews:
                if review.id == review.self.id:
                    revlist.append(review)
            return revlist

        @property
        def amenities(self):
            """Amenity getter method"""
            from models import storage
            from models.amenity import Amenity
            amenis = []
            for amenity in storage.all(Amenity):
                if amenity.amenity_ids in self.id:
                    amenis.append(amenity)
            return amenis

        @amenities.setter
        def amenities(self, obj):
            """Amenity setter method"""
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
