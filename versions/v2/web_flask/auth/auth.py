#!/usr/bin/python3
"""
AUTH module
"""

from flask import Blueprint, render_template
from flask import redirect, url_for, flash, request, jsonify
from models import storage
from models.models import User, Enrollment
from home import find_images
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.utils import secure_filename
from .forms import SignInForm, SignUpForm
from auth import app_views_auth


import datetime
import os
from operator import attrgetter


auth = Blueprint('auth', __name__)


@app_views_auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    """Sing up function"""
    sign_up_form = SignUpForm()
    if sign_up_form.validate_on_submit():
        name = sign_up_form.name.data
        address = sign_up_form.address.data
        email = sign_up_form.email.data
        phone_number = sign_up_form.phone_number.data
        password = sign_up_form.password.data
        my_dict = {"name": name,
                   "email": email,
                   "phone_number": phone_number,
                   "role": "Student",
                   "password": password,
                   "address": address,
                   "profile_image": "user.avif"}
    
        new_instance = User()
        for key, value in my_dict.items():
            setattr(new_instance, key, value)
        try:
            new_instance.save()
            message = """Account successfully created"""
            flash(message, 'success')
            return redirect(url_for('app_views_home.home'))

        except IntegrityError as e:
            storage.close()
            message = """Account not created, Email already exist"""
            flash(message, 'error')
            return redirect(url_for('app_views_home.home'))
    else:
        message = """Account not created: Both passwords must match."""
        flash(message, 'error')
        return redirect(url_for('app_views_home.home'))


@app_views_auth.route('/login', methods=['GET', 'POST'])
def login_view():
    """Login function"""
    sign_in_form = SignInForm()

    if sign_in_form.validate_on_submit():
        email = sign_in_form.email.data
        password = sign_in_form.password.data
        user = storage.get_object(User, email=email)

        if user:
            if user.verify_password(password=password):
                message = "Successfully Logged In"
                login_user(user)
                flash(message, 'success')
                return redirect(url_for('app_views_home.home'))
            message = "Authentification failed : Password or email incorrect"
            flash(message, "error")
            return redirect(url_for('app_views_home.home'))
        else:
            message = "Account doesn't exist"
            flash(message, "error")
            return redirect(url_for('app_views_home.home'))

@app_views_auth.route('/base', methods=['GET', 'POST'])
def base():
    """Base function"""
    return render_template('base.html')


@login_required
@app_views_auth.route('/log_out', methods=['GET'])
def log_out():
    """User logout Function"""
    logout_user()
    return redirect(url_for('app_views_home.home'))


@login_required
@app_views_auth.route('/profile', methods=['GET', 'POST'])
def profile():
    """User profile Session"""
    if current_user.is_authenticated:
        if request.method == "POST":
            image_directory = os.path.join(
                    'home', 'static', 'img'
            )
            file = request.files.get('profile_image')
            if file:
                _, file_extension = os.path.splitext(file.filename)
                user_id = current_user.id
                filename = secure_filename(f"{user_id}{file_extension}")
                for files in os.listdir(image_directory):
                    img = (files.startswith(user_id) and
                            files != f"{user_id}"
                            f"{file_extension}")
                    if img:
                        os.remove(os.path.join(
                            image_directory, file))
                file.save(os.path.join('home', 'static', 'img',
                                        filename))
                current_user.profile_image = filename

            name = request.form.get('name')
            email = request.form.get('email')
            phone_number = request.form.get('phone_number')
            address = request.form.get('address')
            current_user.name = name
            current_user.email = email
            current_user.phone_number = phone_number
            current_user.address = address
            storage.save()
            return jsonify({"success": True})

        image_directory = os.path.join(
                'home', 'static', 'img')
        user_enrollments = storage.get_object(Enrollment, user_id=current_user.id, all=True)
        progresses = []
        
        if user_enrollments:
            p_programs = [program.program for program in user_enrollments]
            progresses = [program.progress for program in user_enrollments]
        else:
            p_programs = []

        all_programs = []
        i = 0
        for program in p_programs:
            images = find_images(image_directory, program.id)
            
            image = images[0] if len(images) != 0 else 'course-1.jpg'
            all_programs.append({"id": program.id,
                                'image': image, 
                            'students': len(program.enrollments),
                            'total_courses': len(program.courses),
                            'progress': progresses[i],
                            'rating': program.rating,
                            'title': program.name})
            i +=1
        return render_template('profile.html',
                            current_page='dashboard',
                            all_programs=all_programs)
    else:
        return render_template('404.html')
