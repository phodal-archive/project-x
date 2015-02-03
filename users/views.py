#!/usr/bin/env python
#coding=utf-8

from flask import Blueprint, render_template, request, flash, url_for, session
from flask_babel import gettext
from flask_login import login_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from users.forms import RegisterForm, LoginForm
from users.models import User

login_manager = LoginManager()

users_mod = Blueprint('users', __name__, template_folder='templates', url_prefix='', static_folder='static')

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@users_mod.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.objects.get_or_404(email=form.email.data)
        if user and check_password_hash(str(user.password), form.password.data):
            # session['user_id'] = str(user.id)

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
        print form.first_name.data, form.last_name.data, form.email.data, generate_password_hash(form.password.data)
        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    blog="",
                    password=generate_password_hash(form.password.data))
        user.save()
        flash(gettext('Thanks for registering'))
        return redirect('/account', form)
    return render_template('/user/register.html', form=form)

@users_mod.route('/account', methods='GET')
def account(form):
    return render_template('/user/user.html', form=form)