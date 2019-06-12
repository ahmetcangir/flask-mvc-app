# -*- coding: utf-8 -*-
"""Default config file."""

# Project details
CREATOR = "Ahmet Cangir"
PROJECT = "Items Catalog"
VERSION = "0.0.1"

# Server details
PORT = 5001
DEBUG = True
HOST = "0.0.0.0"

# Secret key
SECRET_KEY = "My Super Secret Key"

# Database
SQLALCHEMY_DATABASE_URI = "sqlite:///data/itemcatalog.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
