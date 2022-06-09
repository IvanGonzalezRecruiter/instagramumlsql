import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Planets(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    planet_terrain = Column(String(250))
    planet_population = Column(String(250))
    planet_climate = Column(String(250))
    planet_diameter = Column(String(250))
    planet_rotation_period = Column(String(250))
    planet_orbital_period = Column(String(250))
    planet_gravity = Column(String(250))
    planet_


class Personajes(Base):
    __tablename__ = 'personajes'git add .
    
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    personajes_name = Column(String(250))
    personajes_color_ojos = Column(String(250))
    personajes_color_cabello = Column(String(250))
    
   

class FavoritosPlanets(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    planets_id = Column(Integer, ForeignKey('planetas.id'))
    planets = relationship(Planets)    

class FavoritosPersonajes(Base):
    __tablename__ = 'favoritos_personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    personajes = relationship(Personajes)  

      

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')