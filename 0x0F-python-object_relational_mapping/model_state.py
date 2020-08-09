#!/usr/bin/python3
""" module - class State that inherits from Base """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ subclass State that inherits from Base """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                unique=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
