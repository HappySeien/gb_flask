from flask import Blueprint, render_template
from flask_login import login_required

from services.models import Author

author = Blueprint('author', __name__, url_prefix='/authors')


@author.route('/')
@login_required
def author_list():
    authors = Author.query.all()
    return render_template(
        'author_app/list.html',
        authors=authors
    )