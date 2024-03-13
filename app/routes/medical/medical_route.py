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

# request parser

parser = reqparse.RequestParser()
parser.add_argument("full_name", type=str, help="Client's name")
parser.add_argument("email", type=str, help="Client's email")
parser.add_argument("phone", type=str, help="Client's phone")
parser.add_argument("cover_type", type=str, help="Client's cover type")
parser.add_argument("date_of_birth", type=str, help="Client's date of birth")
parser.add_argument("meeting", type=str, help="Client's meeting prefrance")
parser.add_argument("app_date", type=str, help="Client's appointment date")
parser.add_argument("app_time", type=str, help="Client's appointment time")
parser.add_argument("comment", type=str, help="Client's comment")

class MedicalAppointment(Resource):
    def get(self, id=None):
        if id:
            medical_appointment = Medical.query.filter_by(id=id).first()

            if not medical_appointment:
                return {"error": "Appointment not found"}, 404
            
            appointment_data = {
                "full_name": medical_appointment.full_name,
                "email": medical_appointment.email,
                "phone": medical_appointment.phone,
                "cover_type": medical_appointment.cover_type,
                "date_of_birth": medical_appointment.date_of_birth.strftime("%Y-%m-%d"),
                "meeting":medical_appointment.meeting,
                "app_date": medical_appointment.app_date.strftime("%Y-%m-%d"),
                "app_time": medical_appointment.app_time,
                "comment": medical_appointment.comment
            }

            return {"medical Appointment": appointment_data}, 200
        else:
            medical_appointments = Medical.query.all()

            motorAppointment_list = []

            for appointment in medical_appointments:
                appointment_data ={
                "full_name": appointment.full_name,
                "email": appointment.email,
                "phone": appointment.phone,
                "cover_type": appointment.cover_type,
                "date_of_birth": appointment.date_of_birth.strftime("%Y-%m-%d"),
                "meeting":appointment.meeting,
                "app_date": appointment.app_date.strftime("%Y-%m-%d"),
                "app_time": appointment.app_time,
                "comment": appointment.comment
                }

                motorAppointment_list.append(appointment_data)

            return {"medical Appointment": motorAppointment_list}, 200
        

    def post(self):
        args = parser.parse_args()

        full_name = args["full_name"]
        email = args["email"]
        phone = args["phone"]
        cover_type = args["cover_type"]
        date_of_birth = datetime.strptime(args["date_of_birth"], "%d/%m/%Y").date()
        meeting = args["meeting"]
        app_date = datetime.strptime(args["app_date"], "%d/%m/%Y").date()
        app_time = args["app_time"]
        comment = args["comment"]


        # instance


        medical_appointment = Medical (
            full_name=full_name,
            email=email,
            phone=phone,
            date_of_birth=date_of_birth,
            cover_type=cover_type,
            meeting=meeting,
            app_date=app_date,
            app_time=app_time,
            comment=comment 
        )

        db.session.add(medical_appointment)

        try:
            db.session.commit()
            message = "Medical appointment created successfull"
            statu_code = 201

        except Exception as e:
            db.session.rollback()
            message = "Error creating moto appoinment: " + str(e)

            statu_code = 500


            # constructor

            response_data = {
                "message": message,
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "cover_type": cover_type,
                "date_of_birth": str(date_of_birth),
                "meeting":meeting,
                "app_date": str(app_date),
                "app_time": app_time,
                "comment": comment
            }

            return make_response(jsonify(response_data), statu_code)


    def delete(self):
        pass


api.add_resource(MedicalAppointment, "/medicalAppointmet", "/medicalAppointmet/<int:id>")