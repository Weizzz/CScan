#!/usr/bin/env python

import os
from app import app, agency_collection, manager
#from app import app, manager

from jinja2 import Environment, FileSystemLoader
from flask import render_template
from app.Models.User import User
from app.Helpers.Constant import *

###############################################################################
# Set up environment for Jinja
###############################################################################
# Define the template directory
tpldir = os.path.dirname(os.path.abspath(__file__))+'/templates/'

# Setup the template enviroment
env = Environment(loader=FileSystemLoader(tpldir), trim_blocks=True)

###############################################################################
# Supporting function
###############################################################################
@app.errorhandler(404)
def not_found(error):
    return render('404.html', error=404)

def render(page, form=None, error=None, jsonObject=None, extra=None):
    if error:
        return render_template(page,
                               ), error
    else:
        return render_template(page,
                               form = form,
                               jsonObject = jsonObject,
                               extra = extra)

###############################################################################
# VIEWS/PAGES
###############################################################################
from app.Views import home
from app.Views import aboutus
from app.Views import add
from app.Views import list
