from wtforms import Form, BooleanField, TextField, PasswordField,\
                    validators, ValidationError, SelectField, TextAreaField
from app import agency_collection
from flask import flash
from app.Helpers.Constant import *

class regoForm(Form):
    index       = TextField(INDEX)
    agencyName  = TextField(NAME)
    website     = TextField(WEBSITE)
    location    = TextField(LOCATION) #country
    description = TextAreaField(DESCRIPTION)


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


        checkIndex = agency_collection.find_one({INDEX: float(self.index.data.rstrip())}) if self.index.data.rstrip() is not '' else ''

        if checkIndex:
            flash('Agency already exists and will be updated', 'warning')
            bufferName        = self.agencyName.data.rstrip() or checkIndex[NAME]
            bufferWebsite     = self.website.data.rstrip() or checkIndex[WEBSITE]
            bufferLocation    = self.location.data.rstrip() or checkIndex[LOCATION]
            bufferDescription = self.description.data.rstrip() or checkIndex[DESCRIPTION]

            agency_collection.update({
                                        NAME: self.agencyName.data.rstrip()
                                        }, {
                                            '$set':{
                                            NAME       :   bufferName,
                                            WEBSITE    :   bufferWebsite,
                                            LOCATION   :   bufferLocation,
                                            DESCRIPTION:   bufferDescription

                                        }})

            return True
        else:

            newIndex = agency_collection.count()

            agency = {
                INDEX           : newIndex,
                NAME            : self.agencyName.data.rstrip(),
                WEBSITE         : self.website.data.rstrip(),
                LOCATION        : self.location.data.rstrip(),
                DESCRIPTION     : self.description.data
            }

            # insert into database
            agency_collection.insert_one(agency)

            return True
