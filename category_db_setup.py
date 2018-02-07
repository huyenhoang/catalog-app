import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__= 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'picture': self.picture,
        }

class Categories(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    category = Column(String(80), nullable=False)
    image = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'category': self.category,
            "image": self.image,
        }

class Brands(Base):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    location = Column(String(100))
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    website = Column(String(250))
    industry = relationship(Categories)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'website': self.website,
            'description': self.description,
        }

engine = create_engine('sqlite:///categorywithusers.db')


Base.metadata.create_all(engine)
