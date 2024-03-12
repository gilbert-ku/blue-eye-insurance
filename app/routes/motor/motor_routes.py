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
    def get(self):
        pass
    
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
        
    def delete(self):
        pass


api.add_resource(MotorAppointment, "/motorAppointment", "/motorAppointment/<int:id>")