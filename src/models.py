import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
#

class User(Base):
    __tablename__ = 'User'
    userId = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    password = Column(Integer, nullable=False )
    favoriteId = Column(Integer, ForeignKey("favorite.favoriteId" ))
    favorite = relationship("Favorite")

class Favorite(Base):
    __tablename__ = 'favorite'
    favoriteId = Column(Integer, primary_key=True)
    favoritePlanetId = Column(Integer, ForeignKey("planet.planetId"))
    favoriteCharacterId = Column(Integer, ForeignKey("character.characterId"))
    favoriteVehicleId = Column(Integer, ForeignKey("vehicle.vehicleId"))
    planet = relationship("Planet")
    character = relationship("Character")
    vehicle = relationship("Vehicle")

class Planet(Base):
    __tablename__ = 'planet'
    planetId = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    size = Column(String(250), nullable=False)
    favorite = relationship("Favorite")

class Character(Base):
    __tablename__ = 'character'
    characterId = Column(Integer, primary_key=True)
    name = Column(String(250))
    lastName = Column(String(250))
    birthday = Column(Integer, nullable=False)
    favorite = relationship("Favorite")

class Vehicle(Base):
    __tablename__ = 'vehicle'
    vehicleId = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    size = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=False)
    favorite = relationship("Favorite")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')