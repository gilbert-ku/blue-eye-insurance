from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from app.models.admin.admin import Admin

def authenticate(email, password):
    # Query the database to find the admin by email
    admin = Admin.query.filter_by(email=email).first()

    # Check if admin exists and the password is correct
    if admin and check_password_hash(admin.password, password):
        return admin

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
