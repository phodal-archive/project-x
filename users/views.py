#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, render_template, request, flash, url_for, session
from flask_babel import gettext
from flask_login import current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from server import login_manager
from users.User import User

from users.forms import RegisterForm, LoginForm

users_mod = Blueprint('users', __name__, template_folder='templates', url_prefix='', static_folder='static')


@users_mod.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user_obj = User()
        user = user_obj.get_by_email_w_password(email=form.email.data)
        if user and check_password_hash(str(user.password), form.password.data) and user.is_active:
            login_user(user)
            if 'next' in request.form and request.form['next']:
                return redirect(request.form['next'])
            return redirect(url_for('frontends.home'))

        flash('Wrong email or password', 'danger')
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("/user/login.html", form=form)


@users_mod.route('/register/account', methods=('GET', 'POST'))
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        password_hash = generate_password_hash(form.password.data)
        print form.name.data, form.email.data, password_hash
        user = User(form.name.data, form.email.data, password_hash)

        print user
        user.save()
        flash(gettext('Thanks for registering'))
        return redirect('/account', form)
    return render_template('/user/register.html', form=form)


@users_mod.route('/account', methods='GET')
def account(form):
    return render_template('/user/user.html', form=form)


@users_mod.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect('/login')


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')


@login_manager.user_loader
def load_user(id):
    if id is None:
        redirect('/login')
    user = User()
    user.get_by_id(id)
    if user.is_active():
        return user
    else:
        return None