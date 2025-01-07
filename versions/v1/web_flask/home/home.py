#!/usr/bin/python3
"""
AUTH module
"""

from flask import Blueprint, render_template
from models import storage
from models.models import User
from models.models import Course
from models.models import Program
from home import app_views_home

import re
import os

home = Blueprint('home', __name__)

@app_views_home.route("/")
def home():
    """Home page"""
    image_directory = os.path.join(
            'home', 'static', 'img')
    all_programs = storage.get_object(Program,
                                      distinct_fields=[Program.name], all=True)
    top_subjects = storage.get_object(Course, all=True, limit=8)
    courses_data = []
    for course in top_subjects:
        images = find_images(image_directory, course.id)
        image = images[0] if len(images) != 0 else "cat-5.jpg"
        courses_data.append({'name': course.name,
                            'image': image,
                            'program_id': course.program.id, 
                            'program': course.program.name})
    
    courses = []
    i = 0
    for course in all_programs:
        images = find_images(image_directory, course.id)
        
        image = images[0] if len(images) != 0 else 'course-1.jpg'
        courses.append({"id": course.id,
                        'image': image, 
                        'students': len(course.enrollments),
                        'total_courses': len(course.courses),
                        'rating': course.rating,
                        'title': course.name})
        i+=1
        if i == 6:
            break

    return render_template('index.html', courses_data=courses_data,
                           courses=courses,
                           current_page="home")


@app_views_home.route("/about")
def about():
    """About page"""
    return render_template('about.html', current_page="about")

@app_views_home.route("/programs")
def programs():
    """programs"""
    image_directory = os.path.join(
            'home', 'static', 'img')
    p_programs = storage.get_object(Program,
                                      distinct_fields=[Program.name], all=True)
    all_programs = []
    for program in p_programs:
        images = find_images(image_directory, program.id)
        
        image = images[0] if len(images) != 0 else 'course-1.jpg'
        all_programs.append({"id": program.id,
                            'image': image, 
                        'students': len(program.enrollments),
                        'total_courses': len(program.courses),
                        'rating': program.rating,
                        'title': program.name})
    return render_template('programs.html', all_programs=all_programs,
                           current_page="programs")


@app_views_home.route("/courses")
def courses():
    """Courses page"""
    image_directory = os.path.join(
            'home', 'static', 'img')
    courses_data = []
    subjects = storage.get_object(Course, all=True)
    for course in subjects:
        images = find_images(image_directory, course.id)
        image = images[0] if len(images) != 0 else "cat-5.jpg"
        courses_data.append({'name': course.name,
                            'image': image,
                            'program_id': course.program.id,
                            'program': course.program.name})

    return render_template('courses.html', current_page="courses",
                           courses_data=courses_data)


def find_images(image_directory, start_with):
    """Find image"""
    existing_images = [
        filename for filename in os.listdir(image_directory)
        if filename.startswith(start_with) and
        os.path.isfile(os.path.join(image_directory, filename))
    ]

    def extract_number(file):
        match = re.search(r"(\d+)", file)
        return int(match.group(1)) if match else 0

    existing_images = sorted(existing_images, key=extract_number)
    return existing_images
