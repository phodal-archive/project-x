#!/usr/bin/env python
#coding=utf-8

from flask import Blueprint, render_template
from flask_login import current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required

mod = Blueprint('frontends', __name__, template_folder='templates', url_prefix='', static_folder='static')

@mod.route('/')
def home():
    return render_template('home.html')