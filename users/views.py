#!/usr/bin/env python
#coding=utf-8

from flask import Blueprint, render_template, request, flash
from flask_babel import gettext
from flask_mongoengine.wtf.orm import model_form
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from users.forms import RegisterForm
from users.models import User


users_mod = Blueprint('users', __name__, template_folder='templates', url_prefix='', static_folder='static')

PostForm = model_form(User)

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
        print user
        flash('Thanks for registering')
        return redirect('/account', form=form)
    return render_template('register.html', form=form)

@users_mod.route('/account', methods='GET')
def account(form):
    return render_template('user/user.html', form=form)