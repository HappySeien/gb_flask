from werkzeug.security import generate_password_hash
from flask.cli import AppGroup
import os

custom_cli= AppGroup('custom')


@custom_cli.command('init-db', help='create all db')
def init_db():
    from services.extension import db
    db.create_all()
    print('done')


@custom_cli.command('create-users', help='create users')
def create_users():
    from services.extension import db
    from services.models import User
    test_user = User(username='test_user', email='test@email.com', password=generate_password_hash('1234'))
    db.session.add(test_user)
    db.session.commit()
    print('done')


@custom_cli.command('create-admin', help='create admin')
def create_admin():
    from services.extension import db
    from services.models import User
    admin = User(username='admin', email='test_admin@email.com', is_staff=True)
    admin.password = os.environ.get('ADMIN_PASSWORD') or 'admin'
    db.session.add(admin)
    db.session.commit()
    print('created admin:', admin)


@custom_cli.command('create-tags', help='create tags')
def create_tags():
    from services.extension import db
    from services.models import Tag
    tags = ['test_tag1', 'test_tag2', 'test_tag3', 'test_tag4', 'test_tag5']
    for name in tags:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print('created test tags')
