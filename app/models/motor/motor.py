from app import db
from datetime import datetime, timezone


class Motor(db.Model):
    __tablename__ = 'motors'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    vehicleUse = db.Column(db.String(10), nullable=False)
    cover_type = db.Column(db.String(100), nullable=False)
    year_manufc = db.Column(db.String(10), nullable=False)
    valuation = db.Column(db.Integer)
    meeting = db.Column(db.String(100), nullable=False )
    app_date = db.Column(db.Date, nullable=False)
    app_time = db.Column(db.String, nullable=False)
    comment = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)

    # outdated
    # created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False )



    def to_dict(self):
        return{
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "vehicleUse": self.vehicleUse,
            "cover_type": self.cover_type,
            "year_manufc": self.year_manufc,
            "valuation": self.valuation,
            "meeting": self.meeting,
            "app_date": self.app_date.strftime("%Y-%m-%d"),
            "app_time": self.app_time,
            "comment": self.comment,
            "created_at": self.created_at.strftime("%m/%d/%Y %H:%M:%S")
        }
    