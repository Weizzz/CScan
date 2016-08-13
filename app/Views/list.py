from app import app, agency_collection
from app.Forms.add import regoForm
from flask import request, redirect, url_for
from app.Views.views import render

@app.route('/list')
def list():

    # Query all available candidates
    agencies = agency_collection.find()
    return render('list.html', jsonObject=agencies)
