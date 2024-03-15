from flask import Blueprint,jsonify, make_response
from flask_restful import Resource, Api , reqparse
from app import db
# from app.services.login_services import token_required
from flask_jwt_extended import jwt_required


from app.models.contact.contact import Contact

contact_blueprint = Blueprint("contactUs", __name__, url_prefix="/contact_route")

api = Api(contact_blueprint)

class ContactApi(Resource):
    @jwt_required
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
    
    @jwt_required()
    # @token_required
    def get(self, id=None):
        
        if id:
            contact_appointment = Contact.query.filter_by(id=id).first()

            if not contact_appointment:
                return {"error": "Appointment not found"}, 404
            
            appointment_data = {
                "full_name": contact_appointment.full_name,
                "email": contact_appointment.email,
                "phone": contact_appointment.phone,
                "comment": contact_appointment.comment
            }

            return {"contact Appointment": appointment_data}, 200
        else:
            contact_appointments = Contact.query.all()

            contactAppointment_list = []

            for appointment in contact_appointments:
                appointment_data ={
                "full_name": appointment.full_name,
                "email": appointment.email,
                "phone": appointment.phone,
                "comment": appointment.comment
                }

                contactAppointment_list.append(appointment_data)

            return {"contact Appointment": contactAppointment_list}, 200
    
    # @jwt_required()
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

    @jwt_required()
    def delete(self, id=None):
        try:
            if id is not None:
                appointment = Contact.query.filter_by(id=id).first()

                if not appointment:
                    return make_response("Appointment not found", 404)
                
                db.session.delete(appointment)
                db.session.commit()  

                return make_response("Deleted successfully", 204)

            else:
                appointments = Contact.query.all()

                if not appointments:
                    return make_response("No appointments found", 404)

                for appointment in appointments:
                    db.session.delete(appointment)
                
                db.session.commit()  

                return make_response("Deleted successfully", 204)
                
        except Exception as e:
            db.session.rollback()
            return make_response(f"An error occurred: {str(e)}", 500)

api.add_resource(ContactUs, "/contactUs", "/contactUs/<int:id>")