from app import db

class Investment(db.Model):
    __tablename__ = "investment"

    id = db.Column(db.Integer, primary_key=True) 
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Interger(15), nullable=False)
    no_children = db.Column(db.Interger(15), nullable=False)
    Solution = db.Column(db.String(100), nullable=False)
    meeting = db.Column(db.String(100), nullable=False)
    app_date = db.Column(db.Date, nullable=False) 
    app_time = db.Column(db.Time, nullable=False)  
    comment = db.Column(db.String(300), nullable=False)
