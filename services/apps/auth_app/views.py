from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import logout_user, login_user, login_required, current_user
from sqlalchemy.exc import IntegrityError

from werkzeug.security import check_password_hash
from werkzeug.exceptions import NotFound

from services.models import User
from services.forms import RegistrationForm, LoginForm
from services.extension import db

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register/', methods=['GET', 'POST'], endpoint='register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index.main_page'))
    
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).count():
            form.username.errors.append('username already exists!')
            return render_template('auth_app/register.html', form=form)

        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email already exists!')
            return render_template('auth_app/register.html', form=form)

        user = User(
            username=form.username.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            is_staff=False,
        )
        user.password = form.password.data
        db.session.add(user)

        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception('Could not create user!')
            flash('Could not create user!')
        else:
            current_app.logger.info(f'Created user {user}')
            login_user(user)
            return redirect(url_for('index.main_page'))
        
    return render_template('auth_app/register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index.main_page'))

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one_or_none()

        if user is None:
            flash("username doesn't exist")
            return render_template('auth_app/login.html', form=form)
                                   
        if not user.validate_password(form.password.data):
            flash('invalid username or password')
            return render_template('auth_app/login.html', form=form)
        
        login_user(user)

        return redirect(url_for('index.main_page'))
    
    return render_template('auth_app/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))