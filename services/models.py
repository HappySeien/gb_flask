from flask_login import UserMixin
from .extension import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False, default='')
    last_name = db.Column(db.String(150), nullable=False, default='')
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def __repr__(self):
        return f'<User #{self.id} {self.email!r} staff={self.is_staff}>'
