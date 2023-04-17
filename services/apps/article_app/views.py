from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from services.apps.user_app.views import get_user_name

article = Blueprint('article', __name__, url_prefix='/article')

ARTICLES = {
    1: {
        'title': 'Time for time',
        'text': 'many texts',
        'author': 2
    },
    2: {
        'title': 'Time for relax',
        'text': 'more texts',
        'author': 2
    },
    3: {
        'title': 'Cry In floor',
        'text': 'not many texts',
        'author': 1
    },
    4: {
        'title': 'Crying floor',
        'text': 'fantasy is end',
        'author': 3
    }
}


@article.route('/')
def article_list():
    return render_template(
        'article_app/list.html',
        articles=ARTICLES
    )


@article.route('/<int:pk>')
def get_article(pk: int):
    if pk in ARTICLES:
        article_raw = ARTICLES[pk]
    else:
        raise NotFound(f'Article id:{pk}, not found')
    title = article_raw['title']
    text = article_raw['text']
    author = get_user_name(article_raw['author'])
    return render_template(
        'article_app/details.html',
        title=title,
        text=text,
        author=author
    )
