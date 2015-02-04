#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint, render_template

from server import cache


articles_mod = Blueprint('articles', __name__, template_folder='templates', url_prefix='', static_folder='static')


@articles_mod.route("/articles")
@cache.cached(50)
def articles():
    return render_template("articles.html")
