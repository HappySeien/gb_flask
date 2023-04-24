from werkzeug.security import generate_password_hash

from services.app_manager import create_app
from services.extension import db

app = create_app()


@app.cli.command('init-db', help='create all db')
def init_db():
    db.create_all()


@app.cli.command('create-users', help='create users')
def create_users():
    from services.models import User
    db.session.add(
        User(email='test@email.com', password=generate_password_hash('1234'))
    )
    db.session.commit()
    