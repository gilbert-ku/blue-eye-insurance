from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config.development import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

from app.routes.financial_planning.financial_planning import finacial_blueprint
# register blueprint
app.register_blueprint(finacial_blueprint)