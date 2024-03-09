from app import db

class FinancialPlanning(db.Model):
    __tablename__ = "financialplanning"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    employment = db.Column(db.String, nullable=False)
    meeting = db.Column(db.String, nullable=False)
    app_date = db.Column(db.Date, nullable=False)  
    app_time = db.Column(db.Time, nullable=False)  
    comment = db.Column(db.String, nullable=False)  
