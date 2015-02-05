#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, render_template, request, url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from xunta.articles.forms import ArticleForm

from xunta import cache
from xunta.articles.models import Article, Tag


articles_mod = Blueprint('articles', __name__, template_folder='templates', url_prefix='', static_folder='static')


@articles_mod.route("/articles")
@cache.cached(50)
def articles():
    return render_template("/articles/articles.html")


@articles_mod.route("/create/articles", methods=('GET', 'POST'))
@login_required
def create_articles():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        tag = form.tag.data
        # article_tag = Tag(name=tag, description=tag)
        # article_tag.save()
        article = Article(description=content, tag=tag, title=title, content=content, author=current_user)
        article.save()
        print "try save"
        return redirect(request.args.get("next") or url_for("index"))

    return render_template("/articles/create.html", form=form)
