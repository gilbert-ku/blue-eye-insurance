from app import db
from datetime import datetime, timezone

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    comment = db.Column(db.String(300), nullable=False)
    # created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False )
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)


    def to_dict(self):
        return{
            "id": self.id,
            "full_name": self.full_name,
            "phone": self.phone,
            "email": self.email,
            "comment": self.comment,
            "created_at": self.created_at.strftime("%m/%d/%Y %H:%M:%S")
        }
