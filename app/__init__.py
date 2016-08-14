#!/usr/bin/env python
import sys
import os
from flask import Flask
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages')
from pymongo import MongoClient
from flask.ext.login import LoginManager


###############################################################################
# Configuration
###############################################################################
# Flask application setting
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DEBUG = True,
    SECRET_KEY = 'bebsareawesome',
    USERNAME = 'cscan',
    PASSWORD = 'wallacefucktheworld'
))
app.config.from_envvar('CSCAN_SETTING', silent=True)
app.config['basedir'] = os.path.abspath(os.path.dirname(__file__))

# MongoDB database setting
client = MongoClient()
client = MongoClient('mongodb://cscan:wallacefucktheworld@ds031965.mlab.com:31965/cscandb')
db = client['cscandb']
agency_collection = db['agency']
meta_data = db['metadb']


# Manager authentication with LoginManager
# Handle Login with LoginManager
manager = LoginManager()
manager.init_app(app)
manager.login_view = 'login'

# This import here has to be at the bottom of this file
# To avoid circular references
from app.Views import views
