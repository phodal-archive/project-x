#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_babel import gettext

from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class ArticleForm(Form):
    title = StringField(gettext('Articles title'), validators=[DataRequired()])
    tag = StringField(gettext('Articles tag'))
    slug = StringField(gettext('Slug'))
    content = TextAreaField(gettext('Content'), validators=[DataRequired()])


class CommentForm(Form):
    content = StringField(gettext('Comment title'), validators=[DataRequired()])