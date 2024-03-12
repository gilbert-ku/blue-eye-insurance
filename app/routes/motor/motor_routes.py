from flask import Blueprint,jsonify, make_response
from flask_restful import Resource, Api , reqparse
from datetime import datetime
from app import db

from app.models.motor.motor import Motor

motor_blueprint = Blueprint("motor", __name__, url_prefix="/motor_routes")

api = Api(motor_blueprint)

class MotorApi(Resource):
    def get(self):
        return{"Motor Api": "Welcome to motor Api, This rout is responsible in handling motor appointments"}

api.add_resource(MotorApi, "/")

# request parser

parser = reqparse.RequestParser()
parser.add_argument("full_name", type=str, help="Client's Name")
parser.add_argument("email", type=str, help="Client's email")
parser.add_argument("phone", type=str, help="Client's phone")
parser.add_argument("category", type=str, help="category of insurance name")
parser.add_argument("cover_type", type=str, help="type of cover")
parser.add_argument("year_manufc", type=str, help="motor year of manufac")
parser.add_argument("valuation", type=str, help="Client's car valuation")
parser.add_argument("meeting", type=str, help="Client's meeting prefrance")
parser.add_argument("app_date", type=str, help="Client's appointment date prefrance")
parser.add_argument("app_time", type=str, help="Client's app time prefrance")
parser.add_argument("comment", type=str, help="Client's app comments")

class MotorAppointment(Resource):
    def get(self):
        pass
    
    def post(self):
        
        pass

    def delete(self):
        pass


api.add_resource(MotorAppointment, "/motorAppointment", "/motorAppointment/<int:id>")