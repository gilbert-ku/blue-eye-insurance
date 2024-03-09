from app import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.integer(15), nullable=False)
    comment = db.Column(db.String(300), nullable=False)
