from flask import Blueprint, jsonify, make_response
from flask_restful import Resource, Api, reqparse
from datetime import datetime, date
from app import db
from app.models.investment.investing import Investment

investment_blueprint = Blueprint("investment", __name__, url_prefix="/investment_route")

api = Api(investment_blueprint)

class Investment_planning(Resource):
    def get(self):
        return{"Investment planning": "Welcome to investment api, this route is responsible for educational and saving plans"}
    
api.add_resource(Investment_planning, "/")

parser = reqparse.RequestParser()
parser.add_argument("full_name", type=str, help="Client's Name")
parser.add_argument("email", type=str, help="Client's email")
parser.add_argument("phone", type=str, help="Client's phone")
parser.add_argument("no_children", type=str, help="Client's no_children")
parser.add_argument("solution", type=str, help="Client's solution")
parser.add_argument("meeting", type=str, help="Client's meeting")
parser.add_argument("app_date", type=str, help="Client's app_date")
parser.add_argument("app_time", type=str, help="Client's app_time")

parser.add_argument("comment", type=str, help="Client's commwnt")

class InvestmentAppointment(Resource):
    def get(self):
        
        # get all

        investment_appointment = Investment.query.all()

        appoinment_list = []
        for appointment in investment_appointment:
            appoinment_data = {
                "full_name" : appointment.full_name,
                "email" : appointment.email,
                "phone" : appointment.phone,
                "no_children" : appointment.no_children,
                "solution" : appointment.solution,
                "meeting" : appointment.meeting,
                # Convert app_date to string for response
                "app_date" : appointment.app_date.strftime("%d-%m-%Y"),
                "app_time" : appointment.app_time,
                "comment" : appointment.comment,
            }
            appoinment_list.append(appoinment_data)

        return {"Investment Appointments" : appoinment_list}, 200

    def post(self):
        # Parse the request arguments
        args = parser.parse_args()

        # Access parsed arg
        full_name = args["full_name"]
        email = args["email"]
        phone = args["phone"]
        no_children = args["no_children"]
        solution = args["solution"]
        meeting = args["meeting"]
        app_date = datetime.strptime(args["app_date"], "%m/%d/%Y").date() #convert time to python date object
        app_time = args["app_time"]
        comment = args["comment"]

        # creating an instance of investment model
        investmentPlanning = Investment(
            full_name = full_name,
            email = email,
            phone = phone,
            no_children = no_children,
            solution = solution,
            meeting = meeting,
            app_date = app_date,
            app_time = app_time,
            comment = comment,
        )

        # add the instance to a session

        db.session.add(investmentPlanning)

        try:
            # commit the changes to db
            db.session.commit()
            message = "Investment Planning created successfully."
            status_code = 201

        except Exception as e:
            # Rollback the session in case of error
            db.session.rollback()
            message = "Error creating appointment: " + str(e)
            status_code = 500

        response_data = {
            "message": message,
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "no_children": no_children,
            "solution": solution,
            "meeting": meeting,
            # Convert app_date back to string for response
            "app_date": str(app_date),
            "app_time": app_time,
            "comment": comment
        }

        return make_response(jsonify(response_data), status_code)


    def delete(self, id):
        try:
            invest_appointment = Investment.query.filter_by(id=id).first()

            if not invest_appointment:
                return make_response("Appointment not found")
            db.session.delete(invest_appointment)
            db.session.commit()

            return make_response("Deleted Successfully", 204)
        except Exception as e:
            # rollback an error message
            db.session.rollback()

            return make_response(f"An error occurred: {str(e)}", 500)


api.add_resource(InvestmentAppointment, "/investments", "/investment/<int:id>")