from flask import Blueprint,jsonify, make_response
from flask_restful import Resource, Api , reqparse
from datetime import datetime
from app import db

from app.models.corporate.corporate import Corporate

corporate_blueprint = Blueprint("corporate", __name__, url_prefix="/corporate_routes")

api = Api(corporate_blueprint)

class CorporateApi(Resource):
    def get(self):
        return{"Corporate Appointment Api": "Welcome to corporate Api, This route is responsible in handling corporate appointment"}
    
api.add_resource(CorporateApi, "/")

# request parser

parser = reqparse.RequestParser()
parser.add_argument("full_name", type=str, help="Client's name")
parser.add_argument("company_name", type=str, help="Company name")
parser.add_argument("email", type=str, help="Client's email")
parser.add_argument("phone", type=str, help="Client's phone")
parser.add_argument("cover_type", type=str, help="Client's cover type")
parser.add_argument("meeting", type=str, help="Client's meeting prefrance")
parser.add_argument("app_date", type=str, help="Client's appointment date")
parser.add_argument("app_time", type=str, help="Client's appointment time")
parser.add_argument("comment", type=str, help="Client's comment")

class CorporateAppointment(Resource):
    def get(self):
        pass
    def post(self):
        pass
    def delete(self):
        pass

api.add_resource(CorporateAppointment, "/corporateAppointment", "/corporateAppointment/<int:id>")