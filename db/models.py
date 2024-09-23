from sqlalchemy import (Column, Integer, String, Float, DateTime, ForeignKey)
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from typing import Optional
from db import Base
from datetime import datetime


# class Token(Base):
#     access_token: str
#     token_type: str
#
# class TokenData(Base):
#     username: Optional[str] = None


class User(Base):
    __tablename__ = ("users")
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(55), nullable=False)
    phone_number = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)
    password = Column(String)
    reg_date = Column(DateTime, default=datetime.now())


class Courses(Base):
    __tablename__ = "courses"
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String, nullable=True)
    desc = Column(String, nullable=True)
    lessons = relationship("Lessons", back_populates="course")



class Lessons(Base):
    __tablename__ = "lessons"
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String, nullable=False)
    desc = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"))
    videos = relationship("Video", back_populates="lesson")
    course = relationship("Courses", back_populates="lessons")

class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, autoincrement=True, primary_key=True)
    lesson_id = Column(Integer, ForeignKey('lessons.id'))
    file_path = Column(String, nullable=False)
    lesson = relationship("Lessons", back_populates="videos")


class Cart(Base):
    __tablename__ = "cart"
    id = Column(Integer, autoincrement=True, primary_key=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    buy = Column
