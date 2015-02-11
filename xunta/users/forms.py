#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_babel import gettext

from flask_wtf import Form
from wtforms import PasswordField, StringField
from wtforms.validators import EqualTo, Email, DataRequired
from flask_babel import lazy_gettext as _


class RegisterForm(Form):
    name = StringField(_('Nick Name'), validators=[DataRequired()])
    email = StringField(_('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_('Password'), validators=[DataRequired()])
    confirm = PasswordField(_('Confirm'), validators=[
        DataRequired(),
        EqualTo('password', message=_('Passwords must match'))
    ])

class LoginForm(Form):
    email = StringField(gettext('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(gettext('Password'), validators=[DataRequired()])