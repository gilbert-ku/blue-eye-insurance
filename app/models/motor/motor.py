from app import db
import datetime

class Motor(db.Model):
    __tablename__ = 'motors'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    category = db.Column(db.String(10), nullable=False)
    cover_type = db.Column(db.String(100), nullable=False)
    year_manufc = db.Column(db.String(10), nullable=False)
    valuation = db.Column(db.Integer)
    meeting = db.Column(db.String(100), nullable=False )
    app_date = db.Column(db.Date, nullable=False)
    app_time = db.Column(db.String, nullable=False)
    comment = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False )
