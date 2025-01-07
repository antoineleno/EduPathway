#!/usr/bin/python3
"""init module"""
from flask import Blueprint
import os
import sys


app_views_auth = Blueprint('app_views_auth', __name__, url_prefix='/auth',
                           template_folder='templates',
                           static_folder='../home/static')


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from auth.auth import *

