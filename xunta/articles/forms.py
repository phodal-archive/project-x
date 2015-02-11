#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_babel import gettext

from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from flask_babel import lazy_gettext as _

class ArticleForm(Form):
    title = StringField(_('Articles title'), validators=[DataRequired()])
    tag = StringField(_('Articles tag'))
    slug = StringField(_('Slug'))
    content = TextAreaField(_('Content'), validators=[DataRequired()])


class CommentForm(Form):
    content = StringField(_('Comment title'), validators=[DataRequired()])