from app import db
from datetime import datetime, timezone

class Investment(db.Model):
    __tablename__ = "investment"

    id = db.Column(db.Integer, primary_key=True) 
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    principal_dob = db.Column(db.Date, nullable=False)
    solution = db.Column(db.String(100), nullable=False)
    meeting = db.Column(db.String(100), nullable=False)
    app_date = db.Column(db.Date, nullable=False) 
    app_time = db.Column(db.String, nullable=False)  
    comment = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)


    def to_dict(self):
        return{
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'principal_dob': self.principal_dob.strftime("%Y-%m-%d"),
            'solution': self.solution,
            'meeting': self.meeting,
            'app_date': self.app_date.strftime("%Y-%m-%d"),
            'app_time': self.app_time,
            'comment': self.comment,
            'created_at': self.created_at.strftime("%m/%d%Y %H:%M:%S")
        }