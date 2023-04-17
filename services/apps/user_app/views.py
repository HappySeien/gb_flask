from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users')
USERS = {
    1: {'name': 'Ivan'},
    2: {'name': 'Vladislav'},
    3: {'name': 'Elena'}
}


@user.route('/')
def user_list():
    return render_template(
        'user_app/list.html',
        users=USERS
    )


@user.route('/<int:pk>')
def get_user(pk: int):
    if pk in USERS:
        user_raw = USERS[pk]
    else:
        raise NotFound(f'User id:{pk}, not found')
    return render_template(
        'user_app/details.html',
        user_name=user_raw['name']
    )


def get_user_name(pk: int):
    if pk in USERS:
        user_name = USERS[pk]['name']
    else:
        raise NotFound(f'User id:{pk}, not found')
    return user_name
