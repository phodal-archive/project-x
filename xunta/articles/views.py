#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, render_template, request, url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from xunta.articles.forms import ArticleForm
from xunta import cache
from xunta.articles.models import Article


articles_mod = Blueprint('articles', __name__, template_folder='templates', url_prefix='', static_folder='static')


@articles_mod.route("/articles")
@cache.cached(50)
def articles():
    return render_template("/articles/articles.html")

@articles_mod.route("/create/articles", methods=('GET', 'POST'))
@cache.cached(50)
@login_required
def create_articles():
    form = ArticleForm(request.form)
    print current_user
    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        article = Article(content, title, title, content, current_user)
        article.save()
        return redirect(request.args.get("next") or url_for("index"))

    return render_template("/articles/create.html", form=form)
