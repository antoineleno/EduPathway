#!/usr/bin/python3
"""init module"""
from flask import Blueprint
import os
import sys


app_views_curriculum = Blueprint('app_views_curriculum', __name__, url_prefix='/curriculum',
                           template_folder='templates',
                           static_folder='../home/static')


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from curriculum.curriculum import *

