from app import app, agency_collection
from flask import jsonify, request, json, request, redirect, url_for
from app.Forms.add import regoForm
from app.Views.views import render
from app.Helpers.Constant import *



@app.route('/editAgency', methods=['POST'])
def editAgency():
    if request.method == 'POST':

        index = int(request.json[INDEX])
        entry = {
            'agencyname'      : request.json['agencyname'],
            'website'       : request.json['website'],
            'location'        : request.json['location'],
            'description'   : request.json['description']
        }

        #print(index)
        # Delete agency from agency collection according to index
        #print(agency_collection.find_one({'index':index}))
        agency_collection.update({'index':index}, {'$set':
                        { 'agencyname'  : request.json['agencyname'],
                          'website'     : request.json['website'],
                          'location'    : request.json['location'],
                          'description' : request.json['description']}})

        returnString = str(index)
        # return information to frontend
        return jsonify(returnString = returnString)
