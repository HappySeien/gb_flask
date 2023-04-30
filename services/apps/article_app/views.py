from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound

from services.extension import db

from services.models import Article, Author
from services.forms import CreateArticleForm

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


@article.route('/', methods=['GET'])
def article_list():
    articles = Article.query.all()
    return render_template(
        'article_app/list.html',
        articles=articles
    )


@article.route('/<int:pk>', methods=['GET'])
def get_article(pk: int):
    _article = Article.query.filter_by(id=pk).one_or_none()
    if _article is None:
        raise NotFound(f'Article id:{pk}, not found')
    
    return render_template(
        'article_app/details.html',
        article=_article
    )


@article.route('/create', methods=['GET'])
@login_required
def create_article_form():
    form = CreateArticleForm(request.form)
    return render_template('article_app/create.html', form=form)


@article.route('/create', methods=['POST'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)

    if form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), text=form.text.data)

        if not current_user.author:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.commit()

        _article.author_id = current_user.author.id

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for('article.get_article', pk=_article.id))
    return render_template('article_app/create.html', form=form)
