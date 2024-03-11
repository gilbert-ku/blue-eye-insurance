from app import db
import datetime

class FinancialPlanning(db.Model):
    __tablename__ = "financialplanning"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)  
    employment = db.Column(db.String(100), nullable=False)
    meeting = db.Column(db.String(100), nullable=False)
    app_date = db.Column(db.Date, nullable=False)  
    app_time = db.Column(db.String, nullable=False)  
    comment = db.Column(db.String(300), nullable=False)  
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False )  
