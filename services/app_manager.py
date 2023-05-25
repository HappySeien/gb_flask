from flask import Flask
from flask_migrate import Migrate

from combojsonapi.event import EventPlugin
from combojsonapi.permission import PermissionPlugin
from combojsonapi.spec import ApiSpecPlugin

from .settings import Config
from .apps import VIEWS
from .extension import db, login_manager, flask_bcrypt_, admin, api, csrf
from .models import User
from .commands import custom_cli


def create_app() -> Flask:
    app = Flask(__name__, template_folder='apps/templates', static_folder='apps/static')
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    register_custom_commands(app)
    register_admin_panel(app)
    register_api(app)
    return app


def register_extensions(app):
    db.init_app(app)
    Migrate(app, db, compare_type=True)
    
    csrf.init_app(app)

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


def register_admin_panel(app):
    from services import models
    from services.apps.admin_app.views import TagAdminView, UserAdminView, ArticleAdminView
    admin.init_app(app)

    admin.add_view(ArticleAdminView(models.Article, db.session, category='Models'))
    admin.add_view(TagAdminView(models.Tag, db.session, category='Models'))
    admin.add_view(UserAdminView(models.User, db.session, category='Models'))


def register_api(app):
    from services.api.tag import TagList
    from services.api.tag import TagDetail
    from services.api.user import UserList
    from services.api.user import UserDetail
    from services.api.author import AuthorList
    from services.api.author import AuthorDetail
    from services.api.article import ArticleList
    from services.api.article import ArticleDetail

    api.plugins = [
        EventPlugin(),
        PermissionPlugin(),
        ApiSpecPlugin(
            app=app,
            tags={
                'Tag': 'Tag API',
                'User': 'User API',
                'Author': 'Author API',
                'Article': 'Article API',
            }
        ),
    ]
    
    api.init_app(app)

    api.route(TagList, 'tag_list', '/api/tags/', tag='Tag')
    api.route(TagDetail, 'tag_detail', '/api/tags/<int:id>', tag='Tag')

    api.route(UserList, 'user_list', '/api/users/', tag='User')
    api.route(UserDetail, 'user_detail', '/api/users/<int:id>', tag='User')

    api.route(AuthorList, 'author_list', '/api/authors/', tag='Author')
    api.route(AuthorDetail, 'author_detail', '/api/authors/<int:id>', tag='Author')

    api.route(ArticleList, 'article_list', '/api/articles/', tag='Article')
    api.route(ArticleDetail, 'article_detail', '/api/articles/<int:id>', tag='Article')
