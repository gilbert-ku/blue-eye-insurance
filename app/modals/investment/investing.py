from app import db

class Investment(db.Models):
    __tablename__ = "investment"

    id = db.Column(db.Integer, primary_key=True) 
    full_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    no_children = db.Column(db.Interger(15), nullable=False)
    Solution = db.Column(db.String(50), nullable=False)
    meeting = db.Column(db.String(50), nullable=False)
    app_date = db.Column(db.Date, nullable=False) 
    app_time = db.Column(db.Time, nullable=False)  
    comment = db.Column(db.String, nullable=False)
