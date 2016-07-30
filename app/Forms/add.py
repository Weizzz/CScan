from wtforms import Form, BooleanField, TextField, PasswordField,\
                    validators, ValidationError, SelectField, TextAreaField
from app import agency_collection
from flask import flash
from app.Helpers.Constant import *

class regoForm(Form):
    agencyName  = TextField(NAME, [validators.required()])
    website     = TextField(WEBSITE, [validators.required()])
    location    = TextField(LOCATION, [validators.required()]) #country
    description = TextAreaField(DESCRIPTION, [validators.required()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            message = ''
            for fieldName, errorMessages in self.errors.items():
                for err in errorMessages:
                    message = message + fieldName + ': ' + err + '\n'
            flash(message, 'error')
            return False

        checkName = agency_collection.find_one({NAME: self.agencyName.data.rstrip()})
        if checkName:
            flash('Agency has already been filled', 'warning')
            return False
        else:
            agency = {
                NAME            : self.agencyName.data.rstrip(),
                EMAIL           : self.website.data.rstrip(),
                LOCATION        : self.location.data.rstrip(),
                DESCRIPTION     : self.description.data
            }

            # insert into database
            agency_collection.insert_one(agency)

            return True
