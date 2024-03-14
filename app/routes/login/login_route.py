from flask import Blueprint,jsonify, make_response
from flask_restful import Resource, Api , reqparse
from app.models.admin import admin


login_blueprint = Blueprint("AdminLogin", __name__, url_prefix= "/login_route")
api = Api(login_blueprint)

class LoginRoute(Resource):
    def get(self):
        return{"Blue Eye Insurance Agency": "Admin login route"}
    
api.add_resource(LoginRoute, "/")

parser = reqparse.RequestParser()
parser.add_argument("email", type=str, help="Client's email")
parser.add_argument("password", type=str, help="Client's password")

class AdminLogin(Resource):
    def login(self):
        pass


api.add_resource(AdminLogin, "/adminLogin")