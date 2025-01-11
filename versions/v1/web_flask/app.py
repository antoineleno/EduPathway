#!/usr/bin/python3
"""
APP module
"""
import os
import sys
current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(current_path, '../'))
sys.path.append(parent_path)


from flask import Flask, redirect, url_for
from flask_cors import CORS
from flask_login import LoginManager
from models import storage
from flask_login import current_user
from auth.forms import SignInForm, SignUpForm, ForgotPasswordForm
from models.models import User
from auth import app_views_auth
from admin import app_views_admin
from home import app_views_home
from curriculum import app_views_curriculum
from models.models import Program

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '0.0.0.0'}})
app.secret_key = "a2cf8cf6ad37b0d8eb2b51846aee0e34"

app.register_blueprint(app_views_auth)
app.register_blueprint(app_views_admin)
app.register_blueprint(app_views_home)
app.register_blueprint(app_views_curriculum)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'app_views_auth.login_view'



@app.context_processor
def inject_user():
    """Inject all base variables"""
    all_programs = storage.get_object(Program,
                                      distinct_fields=[Program.name], all=True)
    programs = {program.name: program.id for program in sorted(all_programs,
                                                               key=lambda p: p.name)}

    

    admin_user = storage.get_object(User, role="Admin")
    profile_path = "profile.png"

    if current_user.is_authenticated:
        file_names = os.listdir("home/static/img/")
       
        matching_files = [
            f for f in file_names
            if f.startswith(str(current_user.id)) and '.' in f
        ]
    
        if matching_files:
            profile_path = matching_files[0]

    admin_phone_number = admin_user.phone_number
    admin_address = admin_user.address
    admin_email = admin_user.email


    return {
        'user': current_user,
        'profile_path': profile_path,
        'form': SignUpForm(),
        'sign_in_form': SignInForm(),
        'sign_up_form': SignUpForm(),
        'admin_phone_number': admin_phone_number,
        'admin_address': admin_address,
        'admin_email': admin_email,
        'programs': programs,
        'forgot_password_form': ForgotPasswordForm()
    }


@login_manager.user_loader
def load_user(id):
    """Load current user session"""
    return storage.get_object(User, id=id)


@app.teardown_appcontext
def teardown_db(exception):
    """Close everytime the opened session"""
    try:
        storage.close()
    except Exception as e:
        print("this is the error from tear down {}".format(e))
        pass


@app.route('/')
def home():
    """redirect to home page"""
    return redirect(url_for('app_views_home.home'))


if __name__ == "__main__":
    app.run(debug=True)
