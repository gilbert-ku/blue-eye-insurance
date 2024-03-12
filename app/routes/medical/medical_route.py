from flask import Blueprint,jsonify, make_response
from flask_restful import Resource, Api , reqparse
from datetime import datetime
from app import db

from app.models.medical.medical import Medical

medical_blueprint = Blueprint("medical", __name__, url_prefix="/medical_routes")

api = Api(medical_blueprint)

class MedicalApi(Resource):
    def get(self):
        return{"Medical Appointment Api": "Welcome to Medical Api, This route is responsible in handling medical appointment"}
    
api.add_resource(MedicalApi, "/")

# request parser

parser = reqparse.RequestParser()
parser.add_argument("full_name", type=str, help="Client's name")
parser.add_argument("emai", type=str, help="Client's email")
parser.add_argument("phone", type=str, help="Client's phone")
parser.add_argument("cover_type", type=str, help="Client's cover type")
parser.add_argument("date_of_birth", type=str, help="Client's date of birth")
parser.add_argument("meeting", type=str, help="Client's meeting prefrance")
parser.add_argument("app_date", type=str, help="Client's appointment date")
parser.add_argument("app_time", type=str, help="Client's appointment time")
parser.add_argument("comment", type=str, help="Client's comment")