from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')

app.secret_key = 'some secret salt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/db4flask'

db = SQLAlchemy(app)
manager = LoginManager(app)

from app import views, models

with app.app_context():
    db.drop_all()
    db.create_all()