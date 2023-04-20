from flask import Blueprint, render_template

index = Blueprint('index', __name__, url_prefix='/')


@index.route('/')
def main_page():
    return render_template('main_app/index.html')
