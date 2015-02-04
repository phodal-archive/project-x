#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_babel import gettext

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Email, DataRequired


class PostForm(Form):
    title = StringField(gettext('Articles title'), validators=[DataRequired()])
    tag = StringField(gettext('Articles title'))
    description = StringField(gettext('Description'), validators=[DataRequired(), Email()])
    author = StringField(gettext('Author'), validators=[DataRequired()])
