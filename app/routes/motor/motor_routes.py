from flask import Blueprint,jsonify, make_response
from flask_restful import Resource, Api , reqparse
from datetime import datetime
from app import db
from flask_jwt_extended import jwt_required


from app.models.motor.motor import Motor

motor_blueprint = Blueprint("motor", __name__, url_prefix="/motor_routes")

api = Api(motor_blueprint)

class MotorApi(Resource):
    @jwt_required()
    def get(self):
        return{"Motor Api": "Welcome to motor Api, This rout is responsible in handling motor appointments"}

api.add_resource(MotorApi, "/")

# request parser

parser = reqparse.RequestParser()
parser.add_argument("full_name", type=str, help="Client's Name")
parser.add_argument("email", type=str, help="Client's email")
parser.add_argument("phone", type=str, help="Client's phone")
parser.add_argument("category", type=str, help="category of insurance name")
parser.add_argument("cover_type", type=str, help="type of cover")
parser.add_argument("year_manufc", type=str, help="motor year of manufac")
parser.add_argument("valuation", type=str, help="Client's car valuation")
parser.add_argument("meeting", type=str, help="Client's meeting prefrance")
parser.add_argument("app_date", type=str, help="Client's appointment date prefrance")
parser.add_argument("app_time", type=str, help="Client's app time prefrance")
parser.add_argument("comment", type=str, help="Client's app comments")

class MotorAppointment(Resource):
    @jwt_required()
    def get(self, id=None):
        if id:
            # Retrieve a single appointment by ID
            motor_appointment = Motor.query.filter_by(id=id).first()

            if not motor_appointment:
                return {"error": "Appointment not found"}, 404

            appointment_data = {
                "full_name": motor_appointment.full_name,
                "email": motor_appointment.email,
                "phone": motor_appointment.phone,
                "category": motor_appointment.category,
                "cover_type": motor_appointment.cover_type,
                "year_manufc": motor_appointment.year_manufc,
                "valuation": motor_appointment.valuation,
                "meeting": motor_appointment.meeting,
                "app_date": motor_appointment.app_date.strftime("%Y-%m-%d"),
                "app_time": motor_appointment.app_time,
                "comment": motor_appointment.comment
            }

            return {"motor Appointment": appointment_data}, 200
        else:
            # Retrieve all appointments
            motor_appointments = Motor.query.all()

            motorAppointment_list = []

            for appointment in motor_appointments:
                appointment_data = {
                    "full_name": appointment.full_name,
                    "email": appointment.email,
                    "phone": appointment.phone,
                    "category": appointment.category,
                    "cover_type": appointment.cover_type,
                    "year_manufc": appointment.year_manufc,
                    "valuation": appointment.valuation,
                    "meeting": appointment.meeting,
                    "app_date": appointment.app_date.strftime("%Y-%m-%d"),
                    "app_time": appointment.app_time,
                    "comment": appointment.comment
                }
                motorAppointment_list.append(appointment_data)

            return {"motor Appointments": motorAppointment_list}, 200


    @jwt_required()
    def post(self):

        args = parser.parse_args()

        # access parsed arg
        full_name = args["full_name"]
        email = args["email"]
        phone = args["phone"]
        category = args["category"]
        cover_type = args["cover_type"]
        year_manufc = args["year_manufc"]
        valuation = args["valuation"]
        meeting = args["meeting"]
        app_date = datetime.strptime(args["app_date"], "%m/%d/%Y").date()
        app_time = args["app_time"]
        comment = args["comment"]


        # create an instacne

        motor_appointment = Motor (

            full_name=full_name,
            email=email,
            phone=phone,
            category=category,
            cover_type=cover_type,
            year_manufc=year_manufc,
            valuation=valuation,
            meeting=meeting,
            app_date=app_date,
            app_time=app_time,
            comment=comment
        )

        db.session.add(motor_appointment)

        try:
            db.session.commit()
            message = "Motor appointment created successfully."
            status_code = 201

        except Exception as e:
            db.session.rollback()
            message = "Error creating motor appointment: " + str(e)
            status_code = 500


        # constructor
            
            response_data ={
                "message": message,
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "category": category,
                "cover_type": cover_type,
                "year_manufc": year_manufc,
                "valuation": valuation,
                "meeting":meeting,
                "app_date": str(app_date),
                "app_time": app_time,
                "comment": comment
            }

            # return responce

            return make_response(jsonify(response_data), status_code)

    @jwt_required()   
    def delete(self, id=None):
        try:
            if id is not None: 
                appointment = Motor.query.filter_by(id=id).first()

                if not appointment:
                    return make_response("Appointment not found", 404)
                
                db.session.delete(appointment)

            else:
                appointments = Motor.query.all()

                if not appointment:
                    return make_response("No appointment found", 404)
                
                for appointment in appointments:
                    db.session.delete(appointment)

            db.session.commit()

            return make_response("Deleted successfully", 204)
        
        except Exception as e:
            db.session.rollback()
            return make_response(f"An error occured: {str(e)}", 500)


api.add_resource(MotorAppointment, "/motorAppointment", "/motorAppointment/<int:id>")