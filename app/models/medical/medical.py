from app import db
import datetime

class Medical(db.Model):
    __tablename__ = "medical"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    cover_type = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    meeting = db.Column(db.String(100), nullable=False)
    app_date = db.Column(db.Date, nullable=False)
    app_time = db.Column(db.String, nullable=False)
    comment= db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False )


    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "cover_type": self.cover_type,
            "date_of_birth": self.date_of_birth,
            "meeting": self.meeting,
            "app_date": self.app_date,
            "app_time": self.app_time,
            "comment": self.comment,
            "created_at": self.created_at
        }

