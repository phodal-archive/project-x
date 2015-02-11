#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, render_template, request, g, url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from xunta import cache
from xunta.articles.Comment import Comment

from xunta.articles.forms import ArticleForm, CommentForm
from xunta.articles.Articles import Article, Tag


articles_mod = Blueprint('articles', __name__, template_folder='templates', url_prefix='', static_folder='static')


@articles_mod.route("/articles/")
@cache.cached(1000)
def articles():
    article_obj = Article()
    all_articles = article_obj.get_all_articles()
    user = current_user
    if current_user.is_authenticated():
        user = user.get_mongo_doc()
    return render_template("/articles/article_list.html", articles=all_articles, current_user=user)


@articles_mod.route("/articles/<slug>/")
@cache.cached(100)
def get_article(slug):
    article_obj = Article()
    comment_obj = Comment()

    form = CommentForm(request.form)
    article = article_obj.get_article_by_slug(slug)
    all_comments = comment_obj.get_comment_by_article(article)

    return render_template("/articles/article_detail.html", article=article, form=form, comments=all_comments)


@articles_mod.route("/articles/<slug>/comment", methods=('GET', 'POST'))
@login_required
def get_comment(slug):
    article_obj = Article()
    article = article_obj.get_article_by_slug(slug)
    form = CommentForm(request.form)
    if request.method == 'POST' and current_user.is_authenticated() and form.content.data:
        user = current_user.get_mongo_doc()
        comment = Comment(article=article, content=form.content.data, user=user, vote=1)
        comment.save()
    return redirect(url_for('articles.get_article', slug=slug))


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
        url_slug = article.save()
        return redirect(url_for('articles.get_article', slug=slug))

    return render_template("/articles/create.html", form=form, current_user=user)
