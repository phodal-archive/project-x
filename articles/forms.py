#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_babel import gettext

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Email, DataRequired


class PostForm(Form):
    name = StringField(gettext('Articles Name'), validators=[DataRequired()])
    description = StringField(gettext('Description'), validators=[DataRequired(), Email()])
