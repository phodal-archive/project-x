#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_babel import gettext

from flask_wtf import Form
from wtforms import PasswordField, BooleanField, StringField
from wtforms.fields.html5 import URLField
from wtforms.validators import EqualTo, Email, DataRequired


class RegisterForm(Form):
    name = StringField(gettext('Nick Name'), validators=[DataRequired()])
    email = StringField(gettext('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(gettext('Password'), validators=[DataRequired()])
    confirm = PasswordField(gettext('Confirm'), validators=[
        DataRequired(),
        EqualTo('password', message=gettext('Passwords must match'))
    ])
    accept_tos = BooleanField(gettext('I accept the Terms of Service.'), validators=[DataRequired()])
    # recaptcha = RecaptchaField()


class LoginForm(Form):
    email = StringField(gettext('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(gettext('Password'), validators=[DataRequired()])