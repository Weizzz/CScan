#from app import agency_collection
from hashlib import md5
from flask import flash, url_for
from app.Helpers.Constant import *

class User():
    def __init__(self, userObj):
        self.user = userObj
