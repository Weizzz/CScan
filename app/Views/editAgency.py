from app import app, agency_collection
from flask import jsonify, request, json, request, redirect, url_for
from app.Forms.add import regoForm
from app.Views.views import render
from app.Helpers.Constant import *



@app.route('/editAgency', methods=['POST'])
def editAgency():
    #TODO edit
    if request.method == 'POST':
        index = int(request.json[INDEX])

        #print(index)
        # Delete agency from agency collection according to index
        #print(agency_collection.find_one({'index':index}))
        agency_collection.delete_one({'index':index})

        returnString = str(index)
        # return information to frontend
        return jsonify(returnString = returnString)
