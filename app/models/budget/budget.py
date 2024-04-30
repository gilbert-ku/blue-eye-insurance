from app import db
from datetime import datetime, timezone


class Budget(db.Model):
    id = db.Column(db.Inteder, primary_key=True)
    use_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)

    # adding field for storing bugget allocation for predefine categories
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

    def calculate_budget(self, income):
        # calclating budget absed on predefined %
        tith_budget = income * self.tith_allocation
        self_budget = income * self.self_allocation
        rent_budget = income * self.rent_allocation
        transport_budget = income * self.transport_allocation
        education_budget = income * self.education_allocation
        insurance_budget = income * self.insurance_allocation
        emergency_budget = income * self.emergency_allocation
        clothing_budget = income * self.clothing_allocation
        recreation_budget = income * self.recreation_allocation
        charity_budget = income * self.charity_allocation
        holiday_budget = income * self.holiday_allocation
        miscellaneous = income * self.miscellaneous_allocation

        