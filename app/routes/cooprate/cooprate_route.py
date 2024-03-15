from flask import Blueprint,jsonify, make_response
from flask_restful import Resource, Api , reqparse
from datetime import datetime
from app import db
from flask_jwt_extended import jwt_required


from app.models.corporate.corporate import Corporate

corporate_blueprint = Blueprint("corporate", __name__, url_prefix="/corporate_routes")

api = Api(corporate_blueprint)


class CorporateApi(Resource):
    @jwt_required()
    def get(self):
        return{"Corporate Appointment Api": "Welcome to corporate Api, This route is responsible in handling corporate appointment"}
    
api.add_resource(CorporateApi, "/")

# request parser

parser = reqparse.RequestParser()
parser.add_argument("full_name", type=str, help="Client's name")
parser.add_argument("company_name", type=str, help="Company name")
parser.add_argument("email", type=str, help="Client's email")
parser.add_argument("phone", type=str, help="Client's phone")
parser.add_argument("cover_type", type=str, help="Client's cover type")
parser.add_argument("meeting", type=str, help="Client's meeting prefrance")
parser.add_argument("app_date", type=str, help="Client's appointment date")
parser.add_argument("app_time", type=str, help="Client's appointment time")
parser.add_argument("comment", type=str, help="Client's comment")

class CorporateAppointment(Resource):
    @jwt_required()
    def get(self, id=None):
        if id:
            corporate_appointment = Corporate.query.filter_by(id=id).first()

            if not corporate_appointment:
                return {"error": "Appointment not found"}, 404
            
            appointment_data = {
                "full_name": corporate_appointment.full_name,
                "company_name": corporate_appointment.company_name,
                "email": corporate_appointment.email,
                "phone": corporate_appointment.phone,
                "cover_type": corporate_appointment.cover_type,
                "meeting":corporate_appointment.meeting,
                "app_date": corporate_appointment.app_date.strftime("%Y-%m-%d"),
                "app_time": corporate_appointment.app_time,
                "comment": corporate_appointment.comment
            }

            return {"corporate Appointment": appointment_data}, 200
        else:
            corporate_appointments = Corporate.query.all()

            motorAppointment_list = []

            for appointment in corporate_appointments:
                appointment_data ={
                "full_name": appointment.full_name,
                "email": appointment.email,
                "company_name": appointment.company_name,
                "phone": appointment.phone,
                "cover_type": appointment.cover_type,
                "meeting":appointment.meeting,
                "app_date": appointment.app_date.strftime("%Y-%m-%d"),
                "app_time": appointment.app_time,
                "comment": appointment.comment
                }

                motorAppointment_list.append(appointment_data)

            return {"corporate Appointment": motorAppointment_list}, 200

    # @jwt_required()
    def post(self):
        args = parser.parse_args()

        try:
            full_name = args["full_name"]
            company_name = args["company_name"]
            email = args["email"]
            phone = args["phone"]
            cover_type = args["cover_type"]
            meeting = args["meeting"]
            app_date = datetime.strptime(args["app_date"], "%d/%m/%Y").date()
            app_time = args["app_time"]
            comment = args["comment"]

            medical_appointment = Corporate(
                full_name=full_name,
                company_name=company_name,
                email=email,
                phone=phone,
                cover_type=cover_type,
                meeting=meeting,
                app_date=app_date,
                app_time=app_time,
                comment=comment
            )

            db.session.add(medical_appointment)
            db.session.commit()

            response_data = {
                "message": "Corporate appointment created successfully",
                "full_name": full_name,
                "company_name": company_name,
                "email": email,
                "phone": phone,
                "cover_type": cover_type,
                "meeting": meeting,
                "app_date": str(app_date),
                "app_time": app_time,
                "comment": comment
            }

            return make_response(jsonify(response_data), 201)
        
        except ValueError as e:
            error_message = "Error parsing date: " + str(e)
            return make_response(jsonify({"message": error_message}), 400)
        
        except Exception as e:
            db.session.rollback()
            error_message = "Error creating medical appointment: " + str(e)
            return make_response(jsonify({"message": error_message}), 500)

    @jwt_required()
    def delete(self, id=None):
        
        try:
            if id is not None:
                appointment = Corporate.query.filter_by(id=id).first()

                if not appointment:
                    return make_response("Appointment not found", 404)
                db.session.delete(appointment)
                db.session.commit()  

                return make_response("Deleted successfully", 404)
            else:
                appointments = Corporate.query.all()

                if not appointments:
                    return make_response("No appointments found", 404)

                for appointment in appointments:
                    db.session.delete(appointment)
                
                db.session.commit()  # Committing the deletions

                return make_response("Deleted successfully", 204)
            
        except Exception as e:
            db.session.rollback()
            return make_response(f"An error occurred: {str(e)}", 500)



api.add_resource(CorporateAppointment, "/corporateAppointment", "/corporateAppointment/<int:id>")