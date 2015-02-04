#!/usr/bin/env python
#coding=utf-8

from flask import Blueprint, render_template

from xunta import cache


frontends_mod = Blueprint('frontends', __name__, template_folder='templates', url_prefix='', static_folder='static')

@frontends_mod.route('/')
@cache.cached(50)
def home():
    return render_template('home.html')