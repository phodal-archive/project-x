#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from xunta.articles.forms import ArticleForm
from xunta.articles.Articles import Article


articles_mod = Blueprint('articles', __name__, template_folder='templates', url_prefix='', static_folder='static')


@articles_mod.route("/articles/")
def articles():
    article_obj = Article()
    all_articles = article_obj.get_all_articles()
    return render_template("/articles/article_list.html", articles=all_articles)


@articles_mod.route("/articles/<slug>/")
def get_article(slug):
    article_obj = Article()
    article = article_obj.get_article_by_slug(slug)
    return render_template("/articles/article_detail.html", article=article)


@articles_mod.route("/create/articles/", methods=('GET', 'POST'))
@login_required
def create_articles():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        tag = form.tag.data
        slug = form.slug.data
        # article_tag = Tag(name=tag, description=tag)
        # article_tag.save()
        user = current_user.get_mongo_doc()
        article = Article(description=content, tag=tag, title=title, content=content, author=user, slug=slug)
        url_slug = article.save()
        return redirect("/articles/" + url_slug + "/")

    return render_template("/articles/create.html", form=form)
