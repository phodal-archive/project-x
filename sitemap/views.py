#!/usr/bin/env python
#coding=utf-8

from flask import send_from_directory, request, Blueprint
from server import cache

sitemap_mod = Blueprint('sitemap', __name__, static_folder='', static_url_path='/')

@sitemap_mod.route('/sitemap.xml')
@cache.cached(50)
def sitemap():
    print sitemap_mod.static_folder, request.path[1:]
    return send_from_directory(sitemap_mod.static_folder, request.path[1:])
