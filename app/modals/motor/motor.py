from app import db

class Motor(db.Model):
    __tablename__ = 'motors'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Interger(15), nullable=False)
    category = db.Column(db.String(10), nullable=False)
    cover_type = db.Column(db.String(100), nullable=False)
    year_manufc = db.Column(db.Interger(10), nullable=False)
    valuation = db.Column(db.Interger(50))
    meeting = db.Column(db.String(100), nullable=False )
    app_date = db.Column(db.Date, nullable=False)
    app_time = db.Column(db.Time, nullable=False)
    comment = db.Column(db.String(300), nullable=False)
