#!/usr/bin/python3
"""
FORM module
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from flask_wtf.file import FileRequired


class SignInForm(FlaskForm):
    """Sign In form"""
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class SignUpForm(FlaskForm):
    """Sign Up form"""
    name = StringField('First Name')
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number',
                               validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=6)])
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), Length(min=6),
                    EqualTo('password', message='Passwords must match')]
    )
    address = StringField('address', validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class ForgotPasswordForm(FlaskForm):
    """Forgot Password form"""
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Send me instructions')


class UpdateInfos(FlaskForm):
    """Update user information"""
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password',
                                 validators=[DataRequired(), Length(min=6)])
    profile_picture = FileField('Profile Picture', validators=[FileRequired()])
    user_type = StringField('User Type', validators=[DataRequired()])
    submit = SubmitField('Update Information')
