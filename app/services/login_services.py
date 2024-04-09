from flask import make_response, request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from app.models.admin.admin import Admin
# from functools import wraps
# import app

def authenticate(email, password):
    # Query the database to find the admin by email
    admin = Admin.query.filter_by(email=email).first()

    # Check if admin exists and the password is correct
    if admin and check_password_hash(admin.password, password):
        return admin

    if not admin:
        return make_response("Could not verify", 401, {"WWW-Authenticate" : "Basic realm='Loging required!"})
def identify(payload):
    # Extract admin id from the JWT payload
    admin_id = payload["identity"]
    # Retrieve admin from the database based on the id
    return Admin.query.get(admin_id)

def login(email, password):
    # Authenticate the admin
    admin = authenticate(email, password)

    if admin:
        # Create an access token for the authenticated admin
        access_token = create_access_token(identity=admin.id)
        return access_token

    return None


# i can use this if have one admin

# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         access_token = None


#         if "x-access-token" in request.headers:
#             return request.headers["x-access-token"]
        
#         if not access_token:
#             return jsonify({"message" : "Token is missing!"}), 401
        
#         try:
#             data =jwt.decode(access_token, app.config.from_object(DevelopmentConfig))
#             current_admin = Admin.query.filter_by(id=data[id]).first()

#         except:
#             return jsonify({"message" : "Token is invalid!"}), 401
        
#         return f(current_admin, *args, **kwargs)
    
#     return decorated
