#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_babel import gettext

from flask_wtf import Form
from wtforms import PasswordField, BooleanField, StringField
from wtforms.fields.html5 import URLField
from wtforms.validators import EqualTo, Email, DataRequired


class RegisterForm(Form):
    last_name = StringField(gettext('Last Name'), validators=[DataRequired()])
    first_name = StringField(gettext('First Name'), validators=[DataRequired()])
    email = StringField(gettext('Email'), validators=[DataRequired(), Email()])
    blog = URLField(gettext('Blog'))
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