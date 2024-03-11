from flask import Blueprint, jsonify, make_response
from flask_restful import Resource, Api,reqparse
from datetime import datetime, date
from app import db
from app.models.financial_planning.financial_planning import FinancialPlanning 



finacial_blueprint = Blueprint("financial_planning", __name__)

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


class Finacialplanning(Resource):
    def get(self ):

        # get all users
        financial_planning = FinancialPlanning.query.all()  
        response_dict_list = []
        for appointment in financial_planning:
            response_dict = appointment.to_dict()
            response_dict_list.append(response_dict)
        resp = make_response(
            jsonify(response_dict_list),
            200
        )

        return resp
    
        

        
    
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


    def delete(self, Finacialplanning_id):
        pass

    
api.add_resource(Finacialplanning, "/financial_planning/<int:id>")
