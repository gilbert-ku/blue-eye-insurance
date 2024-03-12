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


