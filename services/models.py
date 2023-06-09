from flask_login import UserMixin
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime

from .extension import db, flask_bcrypt_


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False, default='', server_default='')
    last_name = db.Column(db.String(150), nullable=False, default='', server_default='')
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    _password = db.Column(db.LargeBinary, nullable=True)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship('Author', uselist=False, back_populates='user')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt_.generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return flask_bcrypt_.check_password_hash(self._password, password)


    def __repr__(self):
        return f'<User #{self.id} {self.email!r} staff={self.is_staff}>'


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='author')
    articles = relationship('Article', back_populates='author')

    def __str__(self):
        return self.user.username
    


article_tag_association_table = Table(
    'article_tag_association',
    db.metadata,
    db.Column('article_id', db.Integer, ForeignKey('articles.id'), nullable=False),
    db.Column('tag_id', db.Integer, ForeignKey('tags.id'), nullable=False),
)


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, ForeignKey('authors.id'), nullable=False)
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship('Author', back_populates='articles')
    tags = relationship('Tag', secondary=article_tag_association_table, back_populates='articles')

    def __str__(self):
        return self.title
    

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, default='', server_default='')
    
    articles = relationship('Article', secondary=article_tag_association_table, back_populates='tags')

    def __str__(self):
        return self.name
    