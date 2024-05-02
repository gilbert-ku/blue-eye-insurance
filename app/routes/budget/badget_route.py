from flask import Blueprint, jsonify, make_response
from flask_restful import Resource, Api, reqparse
# from app.models.budget.budget import Budget

from app.models.budget.budget_model import Budget

budget_blueprint = Blueprint("budget_route", __name__, url_prefix="/budget_route")

api = Api(budget_blueprint)


class BudgetApi(Resource):
    def get(self):
        return{"Budget Route" : "Welcome to Financial planning budgeting route"}
    
api.add_resource(BudgetApi, "/")


parser = reqparse.RequestParser()

# clent details
parser.add_argument("User_name", type=str, help="Client Fill name")
parser.add_argument("email", type=str, help="client's Email")
parser.add_argument("phone_number", type=str, help="Client's phone number")

# budget allocation

parser.add_argument("tith", type=float, help="allocate tith 10%")
parser.add_argument("self", type=float, help="allocate self 20%")
parser.add_argument("rent", type=float, help="allocate rent 20%")
parser.add_argument("transport", type=float, help="allocate transport 5%")
parser.add_argument("education", type=float, help="allocate education 10%")
parser.add_argument("insurance", type=float, help="allocate insurance 5%")
parser.add_argument("emergency", type=float, help="allocate emergency 5%")
parser.add_argument("clothing", type=float, help="allocate clothing 5%")
parser.add_argument("recreation", type=float, help="allocate recreation 5%")
parser.add_argument("charity", type=float, help="allocate charity 5%")
parser.add_argument("holiday", type=float, help="allocate holiday 5%")
parser.add_argument("miscellaneous", type=float, help="allocation miscellaneous 5%")

