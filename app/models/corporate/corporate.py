from app import db
import datetime

class Corporate(db.Model):
    __tablename__ = "corporate"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    cover_type = db.Column(db.String(100), nullable=False)
    meeting = db.Column(db.String(100), nullable=False )
    app_date = db.Column(db.Date, nullable=False)
    app_time = db.Column(db.String, nullable=False)
    comment = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False )


    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "company_name": self.company_name,
            "email": self.email,
            "phone": self.phone,
            "cover_type": self.cover_type,
            "meeting": self.meeting,
            "app_date": self.app_date.strftime("%m%d%Y"),
            "app_time": self.app_time,
            "comment": self.comment,
            "created_at": self.created_at.strftime("%m/%d/%Y %H:%M:%S")
        }