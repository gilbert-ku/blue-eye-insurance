from flask import Blueprint, jsonify, make_response
from flask_restful import Resource, Api,reqparse
from datetime import datetime, date
from app import db
from app.models.financial_planning.financial_planning import FinancialPlanning 



finacial_blueprint = Blueprint("financial_planning", __name__, url_prefix='/financial_planning')

api = Api(finacial_blueprint)

class Welcome(Resource):
    def get(self):
        return{"Financial Planning": "welcome to financial planning route"}
    
api.add_resource(Welcome, "/")


# Request parser for handling POST and PUT requests
parser = reqparse.RequestParser()
parser.add_argument("full_name", type=str, help="client's Name")
parser.add_argument("email", type=str, help="client's email")
parser.add_argument('phone', type=str, help="Client's phone number")
parser.add_argument("employment", type=str, help="Client's empolyment status")
parser.add_argument("meeting", type=str, help="type of meeting")
parser.add_argument("app_date", type=str, help="Client's appointment date")
parser.add_argument("app_time", type=str, help="Client's appointment time")
parser.add_argument("comment", type=str, help="client's comment and question")


class FinancialPlanningAppointment(Resource):
    # def get(self, id=None):
    #     if id is None:
    #         # Get all financial planning appointments
    #         financial_planning = FinancialPlanning.query.all()
    #         response_dict_list = [appointment.to_dict() for appointment in financial_planning]
    #         return jsonify(response_dict_list), 200
    #     else:
    #         # Get financial planning appointment by id
    #         financial_planning = FinancialPlanning.query.filter_by(id=id).first()

    #         if financial_planning:
    #             response = make_response(jsonify(financial_planning.to_dict()), 200)
    #             return response
    #         else:
    #             response = make_response(jsonify({"error": "Financial planning appointment not found"}), 404)
    #             return response
    
    def get(self):
        # Get all financial planning appointments

        financial_planning = FinancialPlanning.query.all()
        appointment_list = []
        for appointment in financial_planning:
            appointment_data = {
                "full_name": appointment.full_name,
                "email": appointment.email,
                "phone": appointment.phone,
                "employment": appointment.employment,
                "meeting": appointment.meeting,
                "app_date": appointment.app_date.strftime('%Y-%m-%d'),  # Convert app_date to string for response
                "app_time": appointment.app_time,
                "comment": appointment.comment
            }
            appointment_list.append(appointment_data)

        return {"Financial Planning Appointments": appointment_list}, 200

    def post(self):
    # Parse the request arguments
        args = parser.parse_args()

        # Access parsed arguments and perform further processing
        full_name = args["full_name"]
        email = args["email"]
        phone = args["phone"]
        employment = args["employment"]
        meeting = args["meeting"]
        app_date = datetime.strptime(args["app_date"], "%m/%d/%Y").date()
        app_time = args["app_time"]
        comment = args["comment"]

        # Create an instance of the FinancialPlanning model
        financialplanning = FinancialPlanning(
            full_name=full_name,
            email=email,
            phone=phone,
            employment=employment,
            meeting=meeting,
            app_date=app_date,
            app_time=app_time,
            comment=comment
        )

        # Add the instance to the session
        db.session.add(financialplanning)

        try:
            # Commit the changes to the database
            db.session.commit()
            message = "FinancialPlanning created successfully."
            status_code = 201
        except Exception as e:
            # Rollback the session in case of an error
            db.session.rollback()
            message = "Error creating appointment: " + str(e)
            status_code = 500

        # Construct response JSON object
        response_data = {
            "message": message,
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "employment": employment,
            "meeting": meeting,
            "app_date": str(app_date),  # Convert app_date back to string for response
            "app_time": app_time,
            "comment": comment
        }

        # Return response with parsed arguments and message
        return make_response(jsonify(response_data), status_code)

    def delete(self, id=None):
        try:
            if id is not None:
                appointment = FinancialPlanning.query.filter_by(id=id).first()

                if not appointment:
                    return make_response("Appointment not found", 404)

                db.session.delete(appointment)
            else:
                appointments = FinancialPlanning.query.all()

                if not appointments:
                    return make_response("No appointments found", 404)

                for appointment in appointments:
                    db.session.delete(appointment)

            db.session.commit()

            return make_response("Deleted successfully", 204)
        except Exception as e:
            db.session.rollback()
            return make_response(f"An error occurred: {str(e)}", 500)


    
api.add_resource(FinancialPlanningAppointment, "/financial_planning", "/financial_planning/<int:id>")
