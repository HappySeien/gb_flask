from werkzeug.security import generate_password_hash
from flask.cli import AppGroup

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
    test_user = User(email='test@email.com', password=generate_password_hash('1234'))
    test_admin = User(email='test_admin@email.com', password=generate_password_hash('admin'), is_staff=True)
    db.session.add(test_user)
    db.session.add(test_admin)
    db.session.commit()
    print('done')
