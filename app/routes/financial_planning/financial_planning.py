from flask import Blueprint
from flask_restful import Resource, Api,reqparse
import phonenumbers



finacial_blueprint = Blueprint("financial_planning", __name__)

api = Api(finacial_blueprint)

class Welcome(Resource):
    def get(self):
        return{"BEIA": "your one stop insurance provider"}
    
api.add_resource(Welcome, "/")

def validate_phone(value):
    try:
        parsed_number = phonenumbers.parse(value, None)  # 'None' means the number is not associated with any particular region
        if not phonenumbers.is_valid_number(parsed_number):
            raise ValueError()
    except:
        raise ValueError("Invalid phone number")




# Request parser for handling POST and PUT requests
parser = reqparse.RequestParser()
parser.add_argument("full_name", type=str, help="client's Name")
parser.add_argument("email", type=str, help="client's email")
parser.add_argument('phone', type=validate_phone, help="Client's phone number")
parser.add_argument("employment", type=str, help="Client's empolyment status")
parser.add_argument("meeting", type=str, help="type of meeting")
parser.add_argument("app_date", type=str, help="Client's appointment date")
parser.add_argument("app_time", type=str, help="Client's appointment time")
parser.add_argument("comment", type=str, help="client's comment and question")


class Finacialplanning(Resource):
    def get(self, Finacialplanning_id):
        return{"message": "welcome to blue insurance financial planning"}
    
    def post(self):
        pass
    
    def delete(self, Finacialplanning_id):
        pass

    
api.add_resource(Finacialplanning, "/financial_planing")