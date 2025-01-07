#!/usr/bin/python3
"""init module"""
from flask import Blueprint
import os
import sys


app_views_home = Blueprint('app_views_home', __name__, url_prefix='/home',
                           template_folder='templates',
                           static_folder='static')


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from home.home import *

