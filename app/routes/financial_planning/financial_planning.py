from flask import Blueprint
from flask_restful import Resource, Api




finacial_blueprint = Blueprint("financial_planning", __name__)

api = Api(finacial_blueprint)

class Welcome(Resource):
    def get(self):
        return{"BEIA": "your one stop insurance provider"}
    
api.add_resource(Welcome, "/")

class Finacialplanning(Resource):
    def get(self):
        return{"message": "welcome to blue insurance financial planning"}
    
api.add_resource(Finacialplanning, "/financial_planing")