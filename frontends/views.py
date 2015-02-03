#!/usr/bin/env python
#coding=utf-8

from flask import Blueprint, render_template

mod = Blueprint('frontends', __name__, template_folder='templates', url_prefix='', static_folder='static')

@mod.route('/')
def home():
    return render_template('home.html')