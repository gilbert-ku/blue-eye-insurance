from app import db
from datetime import datetime, timezone


class Budget(db.Model):
    id = db.Column(db.Inteder, primary_key=True)
    use_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    # adding field for storing bugget allocation for predefine categories
    # housing_allocation = db.Column(db.Float, nullable=False, default=0.30)
    # food_allocation = db.Column(db.Float, nullable=False, default=0.20)
    # transportation_allocation = db.Column(db.Float, nullable=False, default=0.10)
    # entertainment_allocation = db.Column(db.Float, nullable=False, default=0.15)

    tith_allocation = db.Column(db.Float, nullable=False, default=0.10)
    self_allocation = db.Column(db.Float, nullable=False, default=0.20)
    rent_allocation = db.Column(db.Float, nullable=False, default=0.20)
    transport_allocation = db.Column(db.Float, nullable=False, default=0.05)
    education_allocation = db.Column(db.Float, nullble=False, default=0.10)
    insurance_allocation = db.Column(db.Float, nullable=False, default=0.05)
    emergency_allocation = db.Column(db.Float, nullable=False, default=0.05)
    clothing_allocation = db.Column(db.Flaot, nullable=False, default=0.05)
    recreation_allocation = db.Column(db.Float, nullable=False, default=0.05)
    charity_allocation = db.Column(db.Float, nullable=False, default=0.05)
    holiday_allocation = db.Column(db.Float, nullable=False, default=0.05)
    miscellaneous_allocation = db.Column(db.Float, nullable=False, default=0.05)