from flask import Flask
from flask_migrate import Migrate

from .settings import Config
from .apps import VIEWS
from .extension import db, login_manager, flask_bcrypt_
from .models import User
from .commands import custom_cli


def create_app() -> Flask:
    app = Flask(__name__, template_folder='apps/templates', static_folder='apps/static')
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    register_custom_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    Migrate(app, db, compare_type=True)

    flask_bcrypt_.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)


def register_custom_commands(app: Flask):
    app.cli.add_command(custom_cli)
