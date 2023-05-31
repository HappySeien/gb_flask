from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from flask_combo_jsonapi import Api
from flask_wtf import CSRFProtect

from services.apps.admin_app.views import CustomAdminIndexView

db = SQLAlchemy()
login_manager = LoginManager()
flask_bcrypt_ = Bcrypt()
csrf = CSRFProtect()
admin = Admin(
    name = 'Admin panel',
    template_mode='bootstrap4',
    index_view=CustomAdminIndexView()
)

api = Api()
