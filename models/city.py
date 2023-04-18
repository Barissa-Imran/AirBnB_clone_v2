#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name

    Attributes:
        __tablename__(str): The name of the MySQL table to store Cities.
        name (String): the name of the city.
        state_id (string): The state id of the city
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"),
                      nullable=False)
