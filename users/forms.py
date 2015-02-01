from flask_wtf import Form, RecaptchaField
from wtforms import PasswordField, BooleanField, StringField
from wtforms.fields.html5 import URLField
from wtforms.validators import EqualTo, Email, DataRequired

class RegisterForm(Form):
    last_name = StringField('NickName', validators=[DataRequired()])
    first_name = StringField('NickName', validators=[DataRequired()])
    blog = URLField('blog', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Repeat Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match')
    ])
    accept_tos = BooleanField('I accept the Terms of Service.', validators=[DataRequired()])
    # recaptcha = RecaptchaField()