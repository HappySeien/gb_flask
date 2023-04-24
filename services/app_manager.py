from flask import Flask

from .settings import Config
from .apps import VIEWS
from .extension import db, login_manager
from .models import User


def create_app() -> Flask:
    app = Flask(__name__, template_folder='apps/templates', static_folder='apps/static')
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)
