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