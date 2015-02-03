 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import PasswordField, BooleanField, StringField
from wtforms.fields.html5 import URLField
from wtforms.validators import EqualTo, Email, DataRequired


class RegisterForm(Form):
    last_name = StringField('Last Name', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    blog = URLField('Blog', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Confirm', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match')
    ])
    accept_tos = BooleanField('I accept the Terms of Service.', validators=[DataRequired()])
    # recaptcha = RecaptchaField()