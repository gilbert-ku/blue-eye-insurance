from app import db
from datetime import datetime, timezone
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
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)


    def to_dict(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'employment': self.employment,
            'meeting': self.meeting,
            # Convert date object to string in desired format
            'app_date': self.app_date.strftime("%Y-%m-%d"),  
            'app_time': self.app_time,
            'comment': self.comment,
            # Convert datetime object to string in desired format
            'created_at': self.created_at.strftime("%m/%d/%Y %H:%M:%S")  
        }


# vars() is used to retrive __dict__ attribute of the object

    # def to_dict(self):
    #     return vars(self)