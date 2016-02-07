import flask
import os
from app_factory import AppFactory


def create_app():
    app = flask.Flask(__name__)
    app.environment = os.environ.get('ENVIRONMENT', 'dev')

    AppFactory.setup(app)

    return app
