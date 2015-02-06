#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from xunta import cache

from xunta.articles.forms import ArticleForm
from xunta.articles.Articles import Article, Tag


articles_mod = Blueprint('articles', __name__, template_folder='templates', url_prefix='', static_folder='static')


@articles_mod.route("/articles/")
@cache.cached(1000)
def articles():
    article_obj = Article()
    all_articles = article_obj.get_all_articles()
    user = current_user.get_mongo_doc()
    return render_template("/articles/article_list.html", articles=all_articles, current_user=user)


@articles_mod.route("/articles/<slug>/")
@cache.cached(100)
def get_article(slug):
    article_obj = Article()
    article = article_obj.get_article_by_slug(slug)
    return render_template("/articles/article_detail.html", article=article)


@articles_mod.route("/articles/<slug>/comments", methods=('GET', 'POST'))
def get_comment(slug):
    article_obj = Article()
    article = article_obj.get_article_by_slug(slug)
    return render_template("/articles/article_detail.html", article=article)


def save_tag(tag):
    article_tag = Tag(name=tag, description=tag)
    article_tag.save()
    return article_tag.get_mongo_doc()


@articles_mod.route("/create/articles/", methods=('GET', 'POST'))
@login_required
def create_articles():
    form = ArticleForm(request.form)
    user = current_user.get_mongo_doc()
    if request.method == 'POST' and form.validate():
        title = form.title.data
        content = form.content.data
        tag = form.tag.data
        slug = form.slug.data

        tag = save_tag(tag)

        article = Article(description=content, tag=tag, title=title, content=content, author=user, slug=slug)
        print article
        url_slug = article.save()
        return redirect("/articles/" + url_slug + "/")

    return render_template("/articles/create.html", form=form, current_user=user)
