from flask import Flask

from .apps import VIEWS


def create_app() -> Flask:
    app = Flask(__name__, template_folder='apps/templates', static_folder='apps/static')
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)
