from flask import Blueprint, jsonify, make_response
from flask_restful import Resource, Api, reqparse
from datetime import datetime
from app.models.investment.investing import Investment

investment_blueprint = Blueprint("investment", __name__)

api = Api(investment_blueprint)

class Investment_planning(Resource):
    def get(self):
        return{"Investment planning": "Welcome to investment api, this route is responsible for educational and saving plans"}
    
api.add_resource(Investment_planning, "/")

parser = reqparse.RequestParser()
parser.add_argument("full_name", type=str, help="Client's Name")
parser.add_argument("email", type=str, help="Client's email")
parser.add_argument("phone", type=str, help="Client's phone")
parser.add_argument("no_children", type=str, help="Client's no_children")
parser.add_argument("solution", type=str, help="Client's solution")
parser.add_argument("meeting", type=str, help="Client's meeting")
parser.add_argument("app_date", type=str, help="Client's app_date")
parser.add_argument("app_time", type=str, help="Client's app_time")
parser.add_argument("comment", type=str, help="Client's commwnt")

class InvestmentAppointment(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

api.add_resource(InvestmentAppointment, "/investments")