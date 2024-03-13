from flask import Blueprint,jsonify, make_response
from flask_restful import Resource, Api , reqparse
from datetime import datetime
from app import db

from app.models.contact.contact import Contact

contact_blueprint = Blueprint("contactUs", __name__, url_prefix="/contact_route")

api = Api(contact_blueprint)

class ContactApi(Resource):
    def get(self):
        return{"Contact Us Appointment Api": "Welcome to Contact Us Api, This route is responsible in handling Contact Us appointment"}
    
api.add_resource(ContactApi, "/")

# request parser
parser = reqparse.RequestParser()
parser.add_argument("full_name", type=str, help="Client's name")
parser.add_argument("email", type=str, help="Client's email")
parser.add_argument("phone", type=str, help="Client's phone")
parser.add_argument("comment", type=str, help="Client's comment")