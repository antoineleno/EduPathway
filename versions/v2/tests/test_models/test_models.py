#!/usr/bin/python3
"""
test_building : to test building module
"""

import unittest
from datetime import datetime

from models.base_model import BaseModel

from models.models import User, Program, Course
from models.models import Project, Enrollment, Resource
from models.models import Quiz, Option
from models.models import  UserQuiz
from models import storage
from unittest.mock import MagicMock


class TestBaseModel(unittest.TestCase):
    """BaseModel test"""
    def test_instance_creation(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict_contains_correct_keys(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIn("id", obj_dict)
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)
        self.assertIn("__class__", obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_str_method(self):
        user = User(name="Test User", email="test@example.com",
                    role="student", profile_image="image.png")
        self.assertEqual(str(user), f"<User {user.id}>")

    def test_default_role(self):
        user = User(name="Test User", email="test@example.com",
                    role="student", profile_image="image.png")
        self.assertEqual(user.role, "student")

    def test_password_setter(self):
        user = User(name="Test User", email="test@example.com",
                    role="student", profile_image="image.png")
        user.password = "securepassword"
        self.assertTrue(user.verify_password("securepassword"))
        self.assertFalse(user.verify_password("wrongpassword"))

    def test_password_getter(self):
        user = User(name="Test User", email="test@example.com",
                    role="student", profile_image="image.png")
        with self.assertRaises(AttributeError):
            user.password

    def test_empty_password(self):
        user = User(name="Test User", email="lenomadeleineantoine@gmail.com",
                    role="student", profile_image="image.png")
        user.password = ""
        self.assertTrue(user.verify_password(""))



class TestModels(unittest.TestCase):
    """User Model Test"""

    def test_user_creation(self):
        user = User(name="Test User", email="test@example.com",
                    role="student", profile_image="image.png")
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.role, "student")

    def test_password_hashing(self):
        user = User(name="Test User", email="test@example.com",
                    role="student", profile_image="image.png")
        user.password = "my_secure_password"
        self.assertNotEqual(user.password_hash, "my_secure_password")
        self.assertTrue(user.verify_password("my_secure_password"))

    def test_multiple_enrollments(self):
        user = User(name="Test User",
                    address="ddd",
                    phone_number="dd",
                    email="antoinetantoine@example.com",
                    password="lenoantoine",
                    role="student",
                    profile_image="image.png")
        program1 = Program(name="SSA", description="BCS", rating=10, program_picture="iamge")
        program2 = Program(name="SSB", description="BCS", rating=5,
                           program_picture="iamge")
        enrollment1 = Enrollment(user_id=user.id, program_id=program1.id, proress=100)
        enrollment2 = Enrollment(user_id=user.id, program_id=program2.id, progress=100)


    def test_create_course(self):
        user = MagicMock()
        user.id = "user123"
        
        program = MagicMock()
        program.id = "program123"

        course = Course(name="Course 1", description="Course Description", user_id=user.id, program_id=program.id)
        
        course.id = "course123"

        self.assertIsNotNone(course.id)
        self.assertEqual(course.name, "Course 1")
        self.assertEqual(course.user_id, user.id)
        self.assertEqual(course.program_id, program.id)

    def test_create_resource(self):
        course = MagicMock()
        course.id = "course123"
        
        resource = Resource(title="Resource 1", description="Resource Description", course_id=course.id)
        resource.id = "resource123"
        
        self.assertIsNotNone(resource.id)
        self.assertEqual(resource.title, "Resource 1")
        self.assertEqual(resource.description, "Resource Description")
        self.assertEqual(resource.course_id, course.id)

    def test_resource_relationship(self):
        course = MagicMock()
        course.name = "Course 1"
        
        resource = Resource(title="Resource 2", description="Another Resource Description", course_id=course.id)
        resource.course = course
        
        self.assertEqual(resource.course.name, "Course 1")
        self.assertEqual(resource.course_id, course.id)

    def test_create_project(self):
        course = MagicMock()
        course.id = "course123"
        
        project = Project(title="Project 1", task_name="Task 1", description="Project Description", course_id=course.id)
        project.id = "project123"
        
        self.assertIsNotNone(project.id)
        self.assertEqual(project.title, "Project 1")
        self.assertEqual(project.task_name, "Task 1")
        self.assertEqual(project.description, "Project Description")
        self.assertEqual(project.course_id, course.id)

    def test_project_relationship(self):
        course = MagicMock()
        course.name = "Course 1"
        
        project = Project(title="Project 2", task_name="Task 2", description="Another Project Description", course_id=course.id)
        project.course = course
        
        self.assertEqual(project.course.name, "Course 1")
        self.assertEqual(project.course_id, course.id)

    def test_create_quiz(self):
        course = MagicMock()
        course.id = "course123"
        
        quiz = Quiz(title="Quiz 1", question="What is 2 + 2?", answer="4", duration=30, course_id=course.id)
        quiz.id = "quiz123"
        
        self.assertIsNotNone(quiz.id)
        self.assertEqual(quiz.title, "Quiz 1")
        self.assertEqual(quiz.question, "What is 2 + 2?")
        self.assertEqual(quiz.answer, "4")
        self.assertEqual(quiz.duration, 30)
        self.assertEqual(quiz.course_id, course.id)

    def test_quiz_relationship(self):
        course = MagicMock()
        course.name = "Course 1"
        
        quiz = Quiz(title="Quiz 2", question="What is 3 + 3?", answer="6", duration=45, course_id=course.id)
        quiz.course = course
        
        self.assertEqual(quiz.course.name, "Course 1")
        self.assertEqual(quiz.course_id, course.id)

    def test_create_option(self):
        quiz = MagicMock()
        quiz.id = "quiz123"
        
        option = Option(option="Option A", quiz_id=quiz.id)
        option.id = "option123"
        
        self.assertIsNotNone(option.id)
        self.assertEqual(option.option, "Option A")
        self.assertEqual(option.quiz_id, quiz.id)

    def test_option_relationship(self):
        quiz = MagicMock()
        quiz.title = "Quiz 1"
        
        option = Option(option="Option B", quiz_id=quiz.id)
        option.quiz = quiz
        
        self.assertEqual(option.quiz.title, "Quiz 1")
        self.assertEqual(option.quiz_id, quiz.id)

    def test_create_user_quiz(self):
        user = MagicMock()
        user.id = "user123"
        
        course = MagicMock()
        course.id = "course123"
        
        user_quiz = UserQuiz(user_id=user.id, course_id=course.id, score=85)
        
        self.assertIsNotNone(user_quiz.id)
        self.assertEqual(user_quiz.user_id, user.id)
        self.assertEqual(user_quiz.course_id, course.id)
        self.assertEqual(user_quiz.score, 85)

    def test_user_quiz_relationship(self):
        user = MagicMock()
        user.id = "user123"
        
        course = MagicMock()
        course.id = "course123"
        
        user_quiz = UserQuiz(user_id=user.id, course_id=course.id, score=90)
        user_quiz.user = user
        user_quiz.course = course
        
        self.assertEqual(user_quiz.user.id, "user123")
        self.assertEqual(user_quiz.course.id, "course123")
        self.assertEqual(user_quiz.score, 90)