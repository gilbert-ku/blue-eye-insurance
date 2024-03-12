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

# re