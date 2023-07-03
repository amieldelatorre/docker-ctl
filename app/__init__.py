"""Initialise Flask app"""
import os
from flask import Flask
from dotenv import load_dotenv

def create_app():
    """Create the core Flask application"""

    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY")

    with app.app_context():
        from app.controllers import controller
        app.register_blueprint(controller.ctl_blueprint)

    return app