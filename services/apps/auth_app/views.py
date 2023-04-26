from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash

from services.models import User

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))
    
    if request.method == 'GET':
        return render_template(
            'auth_app/login.html'
        )

    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Check your login details')
        return redirect(url_for('.login'))
    
    login_user(user)
    return redirect(url_for('user.profile', pk=user.id))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))