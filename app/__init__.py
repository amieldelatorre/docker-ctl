"""Initialise Flask app"""
import os
from flask import Flask
from app.utils.initialise import pre_run_checks


def create_app():
    """Create the core Flask application"""
    pre_run_checks()

    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY")

    with app.app_context():
        from app.controllers import controller
        app.register_blueprint(controller.ctl_blueprint)

    return app
