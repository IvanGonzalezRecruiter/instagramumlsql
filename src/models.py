import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(100))
    password = Column(String(200))


class Favorties(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    chara_id = Column(Integer, ForeignKey("character.id"))
    planet_id = Column(Integer, ForeignKey('planet.id'))

class Characters(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    gender = Column(String(1))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(10))
    skin_color = Column(String(10))
    eye_color = Column(String(5))
    birth_year = Column(String(10))
    homeworld = Column(String(10))
    url_image = Column(String(2000))

class Planets(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    population = Column(Integer)
    terrain = Column(String(30))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(20))
    climate = Column(String(30))
    surface_water = Column(Integer)
    url_image = Column(String(2000))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
