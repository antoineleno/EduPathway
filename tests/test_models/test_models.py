#!/usr/bin/python3
"""
test_building : to test building module
"""

import unittest
from datetime import datetime

from models.base_model import BaseModel

from models.models import User, Program, Course
from models.models import Project, Enrollment, Resource
from models.models import Quiz
from models.models import  UserQuiz
from models import storage


class TestClear(unittest.TestCase):
    """Clear all after tests"""
    def test_clear(self):
        """Tear down for the entire test suite"""
        storage.drop_all()
        storage.close()


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


class TestUser(unittest.TestCase):
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

    def test_user_relationship_with_enrollments(self):
        user = User(name="Test User", email="test11@example.com",
                    password="antoine", role="student",
                    profile_image="image.png")
        program = Program(name="Computer Science", opened=True,
                          description="This is computer science")
        user.save()
        program.save()
        enrollment = Enrollment(user_id=user.id, program_id=program.id)
        enrollment.save()
        self.assertIn(enrollment, user.enrollments)

    def test_user_relationship_with_courses(self):
        user = User(name="Test User", email="test@example.com",
                    password="lenoantoine", role="student",
                    profile_image="image.png")
        user.save()
        program = Program(name="Bussiness Administration", opened=True,
                          description="This is computer science")
        program.save()
        course = Course(name="Test Course", description="Test course",
                        user_id=user.id, program_id=program.id)
        course.save()
        self.assertIn(course, user.courses)

    def test_multiple_enrollments(self):
        user = User(name="Test User", email="testantoine@example.com",
                    password="lenoantoine", role="student",
                    profile_image="image.png")
        user.save()
        program1 = Program(name="SSA", opened=True, description="BCS")
        program2 = Program(name="SSB", opened=True, description="BCS")
        program1.save()
        program2.save()
        enrollment1 = Enrollment(user_id=user.id, program_id=program1.id)
        enrollment2 = Enrollment(user_id=user.id, program_id=program2.id)
        enrollment1.save()
        enrollment2.save()

        self.assertEqual(len(user.enrollments), 2)

    def test_user_with_no_enrollments(self):
        user = User(name="Test User", email="testhe@example.com",
                    password="ehy", role="student",
                    profile_image="image.png")
        user.save()

        self.assertEqual(len(user.enrollments), 0)

    def test_profile_image(self):
        user = User(name="Test User", email="test@example.com",
                    password="antoine",
                    role="student",
                    profile_image="image.png")
        self.assertEqual(user.profile_image, "image.png")

    def test_user_task_quiz_relationship(self):
        user = User(name="Test User", email="test@examplelast.com",
                    password="antoine",
                    role="student",
                    profile_image="image.png")
        user.save()
        program = Program(name="BBA", opened=True, description="BBA")
        program.save()
        course = Course(name="DBMS", opened=True, description="DBMs",
                        user_id=user.id, program_id=program.id)
        course.save()

        project = Project(title="Hey", course_id=course.id)
        project.save()
        quiz = Quiz(title="Test Quiz", question="Test question",
                    duration=30, course_id=course.id)
        quiz.save()
        task = Task(title="Test Task", instruction="Test instruction",
                    project_id=project.id)
        task.save()

        user_task = UserTask(user_id=user.id, task_id=task.id, score=90)
        user_task.save()

        user_quiz = UserQuiz(user_id=user.id, quiz_id=quiz.id, score=85)
        user_quiz.save()
        self.assertIn(user_task, user.user_tasks)
        self.assertIn(user_quiz, user.user_quizzes)

    def test_user_with_no_quizzes(self):
        user = User(name="Test User", email="tesssst@example.com",
                    password="leno",
                    role="student",
                    profile_image="image.png")
        user.save()
        self.assertEqual(len(user.user_quizzes), 0)


class TestProgram(unittest.TestCase):
    def test_CreateProgram(self):
        program = Program(name="Architecture", opened=True, description="Hey")
        program.save()

    def test_program_creation(self):
        program = Program(name="English", opened=False, description="Englsih")
        program.save()
        self.assertEqual(program.name, "English")


class TestEnrollment(unittest.TestCase):
    def test_enrollment(self):
        user = User(name="Jane Doe", email="test@exadmplelast.com",
                    password="antoine", role="student",
                    profile_image="image.png")
        program = Program(name="Engineering", opened=True, description="Hey")
        user.save()
        program.save()
        enrollment = Enrollment(user_id=user.id, program_id=program.id)
        enrollment.save()
        self.assertEqual(enrollment.user.name, "Jane Doe")
        self.assertEqual(enrollment.program.name, "Engineering")


class TestCourse(unittest.TestCase):
    def test_course(self):
        user = User(name="Jane Doe", email="test@exadmplelast.com",
                    password="antoine", role="student",
                    profile_image="image.png")
        course = Course(title="Data Structures", user_id=user.id,
                        description="Learn about arrays, trees, and graphs.")
        resource = Resource(title="Lecture Notes",
                            url="http://example.com/notes.pdf",
                            course_id=course.id)
        project = Project(title="Final Year Project",
                          description="Build a working web application.",
                          course_id=course.id)
        task = Task(title="Write Tests",
                    description="Write unit tests for all models.",
                    project_id=project.id)
        task_answer = TaskAnswer(task_id=task.id,
                                 answer="Binary search implemented in Python.")
        quiz = Quiz(title="Python Basics Quiz", question="ABCCCE",
                    duration=1, course_id=course.id)

        self.assertEqual(course.title, "Data Structures")
        self.assertIn("arrays", course.description)
        self.assertEqual(resource.title, "Lecture Notes")
        self.assertTrue(resource.url.startswith("http"))
        self.assertEqual(project.title, "Final Year Project")
        self.assertEqual(task.title, "Write Tests")
        self.assertIn("unit tests", task.description)
        self.assertEqual(task_answer.answer,
                         "Binary search implemented in Python.")
        self.assertEqual(quiz.duration, 1)


class TestClearAfter(unittest.TestCase):
    """Clear all after tests"""
    def test_clear_after(self):
        """Tear down for the entire test suite"""
        storage.drop_all()
        storage.close()
