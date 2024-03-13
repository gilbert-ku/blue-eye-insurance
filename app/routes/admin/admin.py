from flask import Blueprint,jsonify, make_response
from flask_restful import Resource, Api , reqparse
from datetime import datetime
from app import db




from app.models.admin.admin import Admin

admin_blueprint = Blueprint("admin", __name__)

api = Api(admin_blueprint)

class BlueEyeInsurance(Resource):
    def get(self):
        return{"Blue Eye Insurance Agency": "Welcome to Blue eye insurance, This route is responsible in handling leads generated from front end forms"}
    
api.add_resource(BlueEyeInsurance, "/")


parser = reqparse.RequestParser()
parser.add_argument("full_name", type=str, help="Client's name")
parser.add_argument("email", type=str, help="Client's email")
parser.add_argument("phone", type=str, help="Client's phone")
parser.add_argument("password", type=str, help="Client's password")


class UserAdmin(Resource):
    def get(self, id=None):
        Admin_appointments = Admin.query.all()

        admin_list = []
        for appointment in Admin_appointments:
            admin_data ={
            "full_name": appointment.full_name,
            "email": appointment.email,
            "phone": appointment.phone,
            "password": appointment.password
            }
            admin_list.append(admin_data)
        return {"Admin Appointment": admin_list}, 200
    
    def post(self):
        args = parser.parse_args()

        try:
            full_name = args["full_name"]
            email = args["email"]
            phone =args["phone"]
            password = args["password"]

            admin_users = Admin (

                full_name = full_name,
                email = email,
                phone = phone,
                password = password
            )

            db.session.add(admin_users)
            db.session.commit()

            admin_data = {
                "message": "Medical appointment created successfully",
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "password": password
            }

            return make_response(jsonify(admin_data), 201)
        
        except ValueError as e :
            error_message = "Error parsing date: " + str(e)
            return make_response(jsonify({"message": error_message}), 400)
        
        except Exception as e:
            db.session.rollback()
            error_message = "Error create admin: " + str(e)
            return make_response(jsonify({"message": error_message}))

api.add_resource(UserAdmin, "/admin")