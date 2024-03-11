from flask import Blueprint, jsonify, make_response
from flask_restful import Resource, Api,reqparse
import phonenumbers
from app.models.financial_planning.financial_planning import FinancialPlanning



finacial_blueprint = Blueprint("financial_planning", __name__)

api = Api(finacial_blueprint)

class Welcome(Resource):
    def get(self):
        return{"BEIA": "your one stop insurance provider"}
    
api.add_resource(Welcome, "/")

# def validate_phone(value):
#     try:
#         parsed_number = phonenumbers.parse(value, None)  # 'None' means the number is not associated with any particular region
#         if not phonenumbers.is_valid_number(parsed_number):
#             raise ValueError()
#     except:
#         raise ValueError("Invalid phone number")




# Request parser for handling POST and PUT requests
parser = reqparse.RequestParser()
parser.add_argument("full_name", type=str, help="client's Name")
parser.add_argument("email", type=str, help="client's email")
# parser.add_argument('phone', type=validate_phone, help="Client's phone number")
parser.add_argument('phone', type=str, help="Client's phone number")
parser.add_argument("employment", type=str, help="Client's empolyment status")
parser.add_argument("meeting", type=str, help="type of meeting")
parser.add_argument("app_date", type=str, help="Client's appointment date")
parser.add_argument("app_time", type=str, help="Client's appointment time")
parser.add_argument("comment", type=str, help="client's comment and question")


class Finacialplanning(Resource):
    def get(self):
        return{"message": "welcome to blue insurance financial planning"}
    
    def post(self):
        # Parse the request arguments
        args = parser.parse_args()

        # Access parsed arguments and perform further processing
        full_name = args["full_name"]
        email = args["email"]
        phone = args["phone"]
        employment = args["employment"]
        meeting = args["meeting"]
        app_date = args["app_date"]
        app_time = args["app_time"]
        comment = args["comment"]

        # Perform additional processing, validation, or database operations
        
        # Construct response JSON object
        response_data = {
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "employment": employment,
            "meeting": meeting,
            "app_date": app_date,
            "app_time": app_time,
            "comment": comment
        }

        # Return response with parsed arguments
        return make_response(jsonify(response_data), 201)

    def delete(self, Finacialplanning_id):
        pass

    
api.add_resource(Finacialplanning, "/financial_planning")
