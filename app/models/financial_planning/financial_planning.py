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


    def to_dict(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'employment': self.employment,
            'meeting': self.meeting,
            'app_date': self.app_date.strftime("%m/%d/%Y"),  # Convert date object to string in desired format
            'app_time': self.app_time,
            'comment': self.comment,
            'created_at': self.created_at.strftime("%m/%d/%Y %H:%M:%S")  # Convert datetime object to string in desired format
        }


# vars() is used to retrive __dict__ attribute of the object

    # def to_dict(self):
    #     return vars(self)