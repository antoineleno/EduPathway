#!/usr/bin/python3
"""init module"""
from flask import Blueprint
import os
import sys


app_views_admin = Blueprint('app_views_admin', __name__, url_prefix='/admin',
                           template_folder='templates',
                           static_folder='../home/static')


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from admin.admin import *

