#!/usr/bin/env python
#coding=utf-8

from flask import send_from_directory, request, Blueprint

mod = Blueprint('sitemap', __name__, static_folder='', static_url_path='/')

@mod.route('/sitemap.xml')
def sitemap():
    print mod.static_folder, request.path[1:]
    return send_from_directory(mod.static_folder, request.path[1:])
