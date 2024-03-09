from app import db

class Medical(db.Modal):
    __tablename__ = "medical"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Interger(15), nullable=False)
    cover_type = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    meeting = db.Column(db.String(50), nullable=False)
    app_date = db.Column(db.Date, nullable=False)
    app_time = db.Column(db.time, nullable=False)
    comment= db.Column(db.String(250), nullable=False)

