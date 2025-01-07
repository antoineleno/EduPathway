#!/usr/bin/python3
"""
AUTH module
"""

from flask import Blueprint, render_template
from flask import redirect, url_for, flash, request
from models import storage
from models.models import Project, Program, Course, Resource, Quiz, Option
from admin import app_views_admin
from werkzeug.utils import secure_filename
from PIL import Image
from flask_login import current_user
import os

admin = Blueprint('admin', __name__)

@app_views_admin.route("/", methods=['POST', 'GET'])
def home():
    """home method"""
    if current_user.is_authenticated:
        if current_user.role == 'Admin':
            courses = storage.get_object(Course, all=True)
            if request.method == "POST":
                form_identifier = request.form.get('form_identifier')
                if form_identifier == "create_program_form":
                    program_name = request.form.get('programName')
                    program_image = request.files.get('programImage')
                    program_description = request.form.get('programDescription')

                    image = Image.open(program_image)
                    if image.size != (600, 400):
                        message = """Program not created, image size should be
                        600 x 400 pixel"""
                        flash(message, "error")
                        return redirect(url_for('app_views_admin.home'))
                    image_directory = os.path.join(
                    'home', 'static', 'img'
                    )
                    program_image.seek(0)
                    _, file_extension = os.path.splitext(program_image.filename)
                    new_program = Program(name=program_name.title(),
                                    description=program_description,
                                    rating=0)
                    filename = secure_filename(f"{new_program.id}{file_extension}")
                    for files in os.listdir(image_directory):
                        img = (files.startswith(new_program.id) and
                                files != f"{new_program.id}"
                                f"{file_extension}")
                        if img:
                            os.remove(os.path.join(
                                image_directory, program_image))

                    program_image.save(os.path.join('home', 'static', 'img',
                                                filename))
                    new_program.program_picture = filename
                    try:
                        new_program.save()
                    except Exception as e:
                        message = """Program not created, Program already exist!"""
                        flash(message, "error")
                        return redirect(url_for('app_views_admin.home'))

                    message = """Program successfully created"""
                    flash(message, 'success')
                    return redirect(url_for('app_views_admin.home'))
                elif form_identifier == "create_course_form":
                    course_name = request.form.get('courseName')
                    course_image = request.files.get('courseImage')
                    course_description = request.form.get('courseDescription')
                    parentProgram = request.form.get('parentProgram')
                    image = Image.open(course_image)
                    if image.size != (400, 250):
                        message = """Program not created, image size should be
                        400 x 250 pixel"""
                        flash(message, "error")
                        return redirect(url_for('app_views_admin.home'))
                    image_directory = os.path.join(
                    'home', 'static', 'img'
                    )
                    course_image.seek(0)
                    program = storage.get_object(Program, name=parentProgram)
                    _, file_extension = os.path.splitext(course_image.filename)
                    new_course = Course(name=course_name.title(),
                                    description=course_description,
                                    user_id=current_user.id,
                                    program_id=program.id)
                    filename = secure_filename(f"{new_course.id}{file_extension}")
                    for files in os.listdir(image_directory):
                        img = (files.startswith(new_course.id) and
                                files != f"{new_course.id}"
                                f"{file_extension}")
                        if img:
                            os.remove(os.path.join(
                                image_directory, course_image))
                    course_image.save(os.path.join('home', 'static', 'img',
                                        filename))
                    try:
                        new_course.save()
                    except Exception as e:
                        message = """Course not created, Course Already exits!"""
                        flash(message, "error")
                        return redirect(url_for('app_views_admin.home'))
                    message = """Course successfully created!"""
                    flash(message, "success")
                    return redirect(url_for('app_views_admin.home'))
                elif form_identifier == "create_resource_form":
                    title = request.form.get('title')
                    parentCourse = request.form.get('parentCourse')
                    course = storage.get_object(Course, name=parentCourse)
                    description = request.form.get('description')
                    new_resource = Resource(title=title, course_id=course.id,
                                            description=description)
                    new_resource.save()
                    message = """Resource Successfully created!"""
                    flash(message, "success")
                    return redirect(url_for('app_views_admin.home'))
                elif form_identifier == "create_project_form":
                    project_name = request.form.get('projectName')
                    task_name = request.form.get('taskName')
                    description = request.form.get('taskDescription')
                    parentCourse = request.form.get('parentCourse')
                    course = storage.get_object(Course, name=parentCourse)
                    new_project = Project(title=project_name, task_name=task_name,
                                        description=description,
                                        course_id=course.id)
                    try:
                        new_project.save()
                    except Exception as e:
                        message = """An error occure while adding a new project"""
                        flash(message, "error")
                        return redirect(url_for('app_views_admin.home'))
                    message = """Project Successfully Created"""
                    flash(message, "success")
                    return redirect(url_for('app_views_admin.home'))
                else:
                    questions = request.form.getlist('questions[]')
                    options = request.form.to_dict(flat=False)['options[0][]']
                    answers = request.form.getlist('answers[]')
                    quiz_name =  request.form.get('quizName')
                    duration = request.form.get('duration')
                    parentCourse = request.form.get('parentCourse')
                    question = questions[0]
                    answer = options[int(answers[0][-1])]
                    try:
                        course = storage.get_object(Course, name=parentCourse)
                        new_quiz = Quiz(title=quiz_name, question=question,
                        answer=answer, duration=duration, course_id=course.id)
                        new_quiz.save()
                        for option in options:
                            new_option = Option(option=option, quiz_id=new_quiz.id)
                            new_option.save()
                    except Exception as e:
                        message = """An error occur while creating the quiz"""
                        flash(message, "error")
                        return redirect(url_for('app_views_admin.home'))
                    message = """Quiz successfully created!"""
                    flash(message, "success")
                    return redirect(url_for('app_views_admin.home'))
            return render_template('admin.html', courses=courses)
        else:
            return render_template('404.html')
    else:
        return render_template('404.html')