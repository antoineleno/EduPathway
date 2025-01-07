#!/usr/bin/python3
"""DB Storage module"""

import os
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.models import User
from models.models import Program
from models.models import Course
from models.models import Project
from models.models import Enrollment
from models.models import Resource, Option

from models.models import Quiz
from models.models import UserQuiz

base_dir = os.path.dirname(__file__)
parent_dir = os.path.join(base_dir, '..', '..')
sys_path = os.path.abspath(parent_dir)

sys.path.append(sys_path)


class DBStorage:
    """DBStorage
    Class to manage objects storage to DB
    """
    __engine = None
    __session = None

    def __init__(self):
        """Contructor method
        """
        env = os.getenv("ENV")
        db = 'edupathway_db'
    
        if env == 'EDUPATHWAY_ENV':
            db = 'edupathway_test_db'

        self.__engine = create_engine(
                    'mysql+mysqldb://edupathway_user:edupathway_pwd@localhost/{}'.format(db),
                    pool_pre_ping=True)


    def all(self, cls=None):
        """all to retrieve all records from DB

        Args:
            cls (string, optional): Object to return. Defaults to None.

        Returns:
            Dict: All records from a database
        """
        allclasses = {
               'BaseModel': BaseModel, 'User': User, 'Program': Program,
               'Course': Course, 'Project': Project, 'Enrollment': Enrollment,
               'Resource': Resource, 'Quiz': Quiz, 'UserQuiz': UserQuiz, 'Option': Option
              }
        obj_result = {}
        cls = cls if not isinstance(cls, str) else allclasses.get(cls)
        if cls is None:
            for cls in allclasses:
                objs = self.__session.query(cls).all()
                for o in objs:
                    obj_result["{}.{}".format(o.name, o.id)] = o
        else:
            objs = self.__session.query(cls).all()
            for o in objs:
                obj_result["{}.{}".format(o.__table__, o.id)] = o
        return obj_result

    def new(self, obj):
        """new : to add an an obj to a session

        Args:
            obj (instance): Obj created to be added
        """
        self.__session.add(obj)

    def save(self):
        """save: method to commit changes to the db
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Method to delete an obj from the db

        Args:
            obj (string): name of the obj. Defaults to None.
        """
        if obj:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(factory)()

    def close(self):
        """close session
        """
        self.__session.close()

    def drop_all(self):
        """drop the test database"""
        Base.metadata.drop_all(self.__engine)
        self.save()


    def get_object(self, cls, sign=None, all=False, order_by=None,
                limit=None, count=False, distinct_fields=None, **kwargs):
        """
        Get all objects or only one object based on filters.
        Optionally count the results.

        Args:
            cls: The model class to query.
            sign: The comparison operator for filtering.
            all: If True, fetches all matching objects.
            order_by: A tuple (column, direction) for sorting
                    (e.g., (cls.created_at, 'desc')).
            limit: An integer specifying the maximum number of results to return.
            count: If True, returns the count of results based on the filters.
            distinct_fields: A list of fields to apply distinct on.
            **kwargs: Key-value pairs for filtering.

        Returns:
            A single object if `all` is False, otherwise a list of objects.
            If `count` is True, returns the count of objects.
        """
        # Default to '==' if no sign is provided
        sign = sign or '=='

        # Valid comparison operators
        operators = {
            '==': lambda key, value: key == value,
            '!=': lambda key, value: key != value,
            '<': lambda key, value: key < value,
            '<=': lambda key, value: key <= value,
            '>': lambda key, value: key > value,
            '>=': lambda key, value: key >= value
        }

        # Start building the query
        query = self.__session.query(cls)

        # Apply filters from kwargs
        if kwargs:
            for key, value in kwargs.items():
                if sign in operators:
                    query = query.filter(operators[sign](getattr(cls, key), value))
                else:
                    raise ValueError(f"Invalid comparison operator: {sign}")

        # Apply distinct (if specified)
        if distinct_fields:
            query = query.distinct(*distinct_fields)

        # Count query (if specified)
        if count:
            return query.count()

        # Apply ordering (if specified)
        if order_by:
            column, direction = order_by
            if direction.lower() == 'desc':
                query = query.order_by(column.desc())
            elif direction.lower() == 'asc':
                query = query.order_by(column)
            else:
                raise ValueError("Invalid direction for order_by")

        # Apply limit (if specified)
        if limit is not None:
            query = query.limit(limit)

        # Return either all results or just the first one
        if all:  # check if all is True
            return query.all()
        return query.first()
