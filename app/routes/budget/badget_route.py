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