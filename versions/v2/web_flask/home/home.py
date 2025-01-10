#!/usr/bin/python3
"""
AUTH module
"""

from flask import Blueprint, render_template
from flask import request, render_template, redirect, url_for, flash
from models import storage
from models.models import Course
from models.models import Program, Room
from home import app_views_home
import random

import re
import os

home = Blueprint('home', __name__)

@app_views_home.route("/", methods=['POST', 'GET'])
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

@app_views_home.route("/programs", methods=['POST', 'GET'])
def programs():
    """programs"""

    if request.method == 'POST':
        search_query = request.form.get('query').title()
        p_programs = storage.get_object(Program, name=search_query, all=True)
    else:
        p_programs = storage.get_object(Program,
                                        distinct_fields=[Program.name], all=True)
    image_directory = os.path.join(
            'home', 'static', 'img')

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


@app_views_home.route("/courses", methods=['POST', 'GET'])
def courses():
    """Courses page"""
    image_directory = os.path.join(
            'home', 'static', 'img')
    courses_data = []
    if request.method == 'POST':
        search_query = request.form.get('query').title()
        subjects = storage.get_object(Course, name=search_query, all=True)
    else:
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


@app_views_home.route("/peer_learning", methods=['POST', 'GET'])
def peer_learning():
    """PL page"""
    if request.method == "POST":
        title = request.form.get('title')
        duration = request.form.get('duration')
        link = request.form.get('link')
        new_room = Room(title=title, duration=duration, link=link)
        try:
            new_room.save()
            message = """Room created successfully"""
            flash(message, "success")
        except Exception as e:
            message = """An unexpected error occured, Room not created"""
            flash(message, "error")
        return redirect(url_for('app_views_home.peer_learning'))

    all_rooms = storage.get_object(Room, all=True)
    room_informations = []

    all_image = find_images("home/static/img/PL", "image")

    for room in all_rooms:
        random_number = random.randint(0, 9)
        duration_in_minutes = int(room.duration)
        hours = duration_in_minutes // 60
        minutes = duration_in_minutes % 60
        if hours > 0:
            duration_string = f"{hours}h {minutes}min left" if minutes > 0 else f"{hours}h left"
        else:
            duration_string = f"{minutes}min left"

        room_informations.append({
            'name': room.title,
            'image_link': all_image[random_number],
            'duration': duration_string,
            'link': room.link
        })

    return render_template('peer_learning.html',
                           room_information=room_informations,
                           current_page="PL")

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
