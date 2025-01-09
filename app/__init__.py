from flask import Flask
from app import views

def create_app():
    app = Flask(__name__, template_folder='templates')
    print("Start Server")
    return app