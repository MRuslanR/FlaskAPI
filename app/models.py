from flask_login import UserMixin

from app import db, manager

class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)