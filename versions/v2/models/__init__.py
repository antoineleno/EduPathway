#!/usr/bin/python3
"""
__init__module
"""
from models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()
