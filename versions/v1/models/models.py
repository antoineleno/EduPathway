#!/usr/bin/python3
"""User module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean, Text, ForeignKey, Integer
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel, Base, UserMixin):
    """Mapping class for user table"""
    __tablename__ = "user"
    name = Column(String(224), nullable=False)
    email = Column(String(224), nullable=False, unique=True)
    address = Column(String(224), nullable=False)
    phone_number = Column(String(224), nullable=False)
    password_hash = Column(String(1024), nullable=False)
    role = Column(String(10), nullable=False)
    profile_image = Column(String(65), nullable=False)

    enrollments = relationship("Enrollment",
                               back_populates="user",
                               cascade="all, delete")
    courses = relationship("Course",
                           back_populates="user",
                           cascade="all, delete")
    user_quizzes = relationship("UserQuiz", back_populates="user",
                                cascade="all, delete")

    @property
    def password(self):
        raise AttributeError('Password is not a readable Attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password=password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password=password)

    def __str__(self):
        return f'<User {self.id}>'


class Program(BaseModel, Base):
    """Mapping class for Program table"""
    __tablename__ = "program"
    name = Column(String(45), nullable=False, unique=True)
    rating = Column(Integer, nullable=False)
    program_picture = Column(String(65), nullable=False)
    description = Column(Text, nullable=False)
    enrollments = relationship("Enrollment", back_populates="program",
                               cascade="all, delete")
    courses = relationship("Course", back_populates="program",
                           cascade="all, delete")


class Enrollment(BaseModel, Base):
    """Mapping class for Enrollment table"""
    __tablename__ = "enrollment"
    user_id = Column(String(60), ForeignKey('user.id', ondelete="CASCADE"),
                     nullable=False)
    program_id = Column(String(60),
                        ForeignKey('program.id', ondelete="CASCADE"),
                        nullable=False)
    progress = Column(Integer, nullable=False)
    user = relationship("User", back_populates="enrollments")
    program = relationship("Program", back_populates="enrollments")


class Course(BaseModel, Base):
    """Mapping class for Course table"""
    __tablename__ = "course"
    name = Column(String(45), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    user_id = Column(String(60), ForeignKey('user.id', ondelete="CASCADE"),
                     nullable=False)
    program_id = Column(String(60),
                        ForeignKey('program.id', ondelete="CASCADE"),
                        nullable=False)
    user = relationship("User", back_populates="courses")
    program = relationship("Program", back_populates="courses")
    resources = relationship("Resource", back_populates="course",
                             cascade="all, delete")
    quizzes = relationship("Quiz", back_populates="course",
                           cascade="all, delete")
    projects = relationship("Project", back_populates="course",
                            cascade="all, delete")
    user_quizzes = relationship("UserQuiz", back_populates="course",
                                cascade="all, delete")

class Resource(BaseModel, Base):
    """Mapping class for Resource table"""
    __tablename__ = "resource"
    title = Column(String(45), nullable=False)
    description = Column(Text, nullable=False)
    course_id = Column(String(60), ForeignKey('course.id', ondelete="CASCADE"),
                       nullable=False)
    course = relationship("Course", back_populates="resources")

class Project(BaseModel, Base):
    """Mapping class for Project table"""
    __tablename__ = "project"
    title = Column(String(45), nullable=False)
    task_name = Column(String(60), nullable=False)
    description = Column(Text, nullable=False)
    course_id = Column(String(60), ForeignKey('course.id', ondelete="CASCADE"),
                       nullable=False)
    course = relationship("Course", back_populates="projects")

class Quiz(BaseModel, Base):
    """Mapping class for Quiz table"""
    __tablename__ = "quiz"
    title = Column(String(45), nullable=False)
    question = Column(Text, nullable=False)
    answer = Column(String(45), nullable=False)
    duration = Column(Integer, nullable=False)
    course_id = Column(String(60), ForeignKey('course.id', ondelete="CASCADE"),
                       nullable=False)
    course = relationship("Course", back_populates="quizzes")
    options = relationship("Option", back_populates="quiz",
                           cascade="all, delete")

class Option(BaseModel, Base):
    """Mapping class for options"""
    __tablename__ = "option"
    option = Column(Text, nullable=False)
    quiz_id = Column(String(60), ForeignKey('quiz.id', ondelete="CASCADE"), nullable=False)
    quiz = relationship("Quiz", back_populates="options")

class UserQuiz(BaseModel, Base):
    """Mapping class for User Quiz"""
    __tablename__ = "user_quiz"
    user_id = Column(String(60), ForeignKey('user.id', ondelete="CASCADE"),
                     nullable=False)
    course_id = Column(String(60), ForeignKey('course.id', ondelete="CASCADE"),
                       nullable=False)
    score = Column(Integer, nullable=False)
    
    user = relationship("User", back_populates="user_quizzes")
    course = relationship("Course", back_populates="user_quizzes")

