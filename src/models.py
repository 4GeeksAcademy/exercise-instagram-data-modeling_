import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))
    post = relationship("Post", back_populates="User")
    comment = relationship("Comment", back_populates="User")

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('User.id')) 
    post_id = Column(Integer, ForeignKey('Post.id'))
    post = relationship("Post", back_populates="comment")
    user = relationship("User", back_populates="comment")

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(250), ForeignKey('User.id'))
    media = relationship("Media", back_populates="post")
    user = relationship("User", back_populates="post")
    Comment = relationship("Comment", back_populates="post")

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum('video', 'picture', name='media_type'))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('Post.id'))
    post = relationship("Post", back_populates="media")
    
class Follower(Base):
    __tablename__ = 'Follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('User.id'))
    user_to_id = Column(Integer, ForeignKey('User.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
