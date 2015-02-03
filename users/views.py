#!/usr/bin/env python
#coding=utf-8

from flask import Blueprint, render_template, request, flash
from flask_babel import gettext
from flask_mongoengine.wtf.orm import model_form
from werkzeug.utils import redirect
from flask_babel import Babel, gettext as _

from users.forms import RegisterForm
from users.models import User


users_mod = Blueprint('users', __name__, template_folder='templates', url_prefix='', static_folder='static')

PostForm = model_form(User)

@users_mod.route('/register/account', methods=('GET', 'POST'))
def add_post():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        flash(gettext('Thanks for registering'))
        return redirect('/register/success')
    return render_template('register.html', form=form)