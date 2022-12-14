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
    userId = Column(Integer, primary_key=True)
    userName = Column(String(50), nullable=False)
    fisrtName = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey("user.userId"))
    user_to_id = Column(Integer, ForeignKey("user.userId"))
    user = relationship("User")

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey("user.useId"))
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post")
    user = relationship("User")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.userId"))
    user = relationship("User")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')