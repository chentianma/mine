from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user
from . import auth
from ..models import User
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        user = User.query.filter_by(name=form.user_name.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', login_form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
