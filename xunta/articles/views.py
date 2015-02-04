#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, render_template, request
from flask_login import login_required

from xunta.articles.forms import PostForm
from xunta import cache


articles_mod = Blueprint('articles', __name__, template_folder='templates', url_prefix='', static_folder='static')


@articles_mod.route("/articles")
@cache.cached(50)
def articles():
    return render_template("/articles/articles.html")

@articles_mod.route("/create/articles", methods=('GET', 'POST'))
@cache.cached(50)
@login_required
def create_articles():
    form = PostForm(request.form)
    if request.method == 'POST' and form.validate():
        print "success create articles"

    return render_template("/articles/create.html", form=form)
