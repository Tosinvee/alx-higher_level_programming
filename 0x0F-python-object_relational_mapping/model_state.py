#!/usr/bin/python3
'''
a python file that contains the class definition of a State and an instance
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declartive_base


class state(Base):
    __tablename__ = 'states'
    id = Column(Integer, auto-increment=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
