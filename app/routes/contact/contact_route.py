from flask import Blueprint,jsonify, make_response
from flask_restful import Resource, Api , reqparse
from datetime import datetime
from app import db

from app.models.contact.contact import Contact

contact_blueprint = Blueprint("contactUs", __name__, url_prefix="/contact_route")

api = Api(contact_blueprint)

class ContactApi(Resource):
    def get(self):
        return{"Contact Us Appointment Api": "Welcome to Contact Us Api, This route is responsible in handling Contact Us appointment"}
    
api.add_resource(ContactApi, "/")

# request parser
parser = reqparse.RequestParser()
parser.add_argument("full_name", type=str, help="Client's name")
parser.add_argument("email", type=str, help="Client's email")
parser.add_argument("phone", type=str, help="Client's phone")
parser.add_argument("comment", type=str, help="Client's comment")

class ContactUs(Resource):
    def get(self):
        pass
    def post(self):
        args = parser.parse_args()

        try:
            full_name = args["full_name"]
            email = args["email"]
            phone = args["phone"]
            comment = args["comment"]

            contact_appointment = Contact(
                full_name=full_name,
                email=email,
                phone=phone,
                comment=comment
            )

            db.session.add(contact_appointment)
            db.session.commit()

            response_data = {
                "message": "Contact appointment created successfully",
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "comment": comment
            }

            return make_response(jsonify(response_data), 201)

        except ValueError as e:
            error_message = "Error parsing date: " + str(e)
            return make_response(jsonify({"message": error_message}), 400)

        except Exception as e:
            db.session.rollback()
            error_message = "Error creating Contact appointment: " + str(e)
            return make_response(jsonify({"message": error_message}), 500)

    def delete(self):
        pass

api.add_resource(ContactUs, "/contactUs", "/contactUs/<int:id>")