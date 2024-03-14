from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config.development import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.routes.financial_planning.financial_planning import finacial_blueprint
from app.routes.investment.investment_routing import investment_blueprint
from app.routes.motor.motor_routes import motor_blueprint
from app.routes.medical.medical_route import medical_blueprint
from app.routes.cooprate.cooprate_route import corporate_blueprint
from app.routes.contact.contact_route import contact_blueprint
from app.routes.admin.admin import admin_blueprint
from app.routes.login.login_route import login_blueprint
# register blueprint
app.register_blueprint(finacial_blueprint)
app.register_blueprint(investment_blueprint)
app.register_blueprint(motor_blueprint)
app.register_blueprint(medical_blueprint)
app.register_blueprint(corporate_blueprint)
app.register_blueprint(contact_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(login_blueprint)
