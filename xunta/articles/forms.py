#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_babel import gettext

from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import Email, DataRequired


class ArticleForm(Form):
    title = StringField(gettext('Articles title'), validators=[DataRequired()])
    tag = StringField(gettext('Articles tag'))
    slug = StringField(gettext('Slug'))
    content = TextAreaField(gettext('Content'), validators=[DataRequired()])