from flask import Blueprint,jsonify, request
from flask_restful import Resource, Api , reqparse
from app.models.admin import admin
from app import db
from app.services.login_services import login
from flask_jwt_extended import jwt_required



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
    def post(self):
        # Get email and password from the request
        email = request.json.get("email", None)
        password = request.json.get("password", None)

        # Check if email and password are provided
        if not email or not password:
            return jsonify({"Message": "Email and password are required"}), 400

        # Authenticate the admin using the login function from services
        access_token = login(email, password)

        if access_token:
            # If authentication is successful, return the JWT token
            return {"token": access_token}, 200
        else:
            # If authentication fails, return an error message
            return {"Message": "Invalid email or password"}, 401
    
api.add_resource(AdminLogin, "/adminLogin")