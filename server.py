#!/usr/bin/env python
#coding=utf-8

from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_babel import Babel
from flask_login import LoginManager
from flask_cache import Cache

from gevent import monkey
from gevent.wsgi import WSGIServer


app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_pyfile('config.cfg')

babel = Babel(app)
toolbar = DebugToolbarExtension(app)

cache = Cache(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def not_found(error):
    return render_template('500.html'), 500

from frontends.views import frontends_mod
app.register_blueprint(frontends_mod)

from sitemap.views import sitemap_mod
app.register_blueprint(sitemap_mod)

from users.models import db
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

from users.views import users_mod
app.register_blueprint(users_mod)

from articles.views import articles_mod
app.register_blueprint(articles_mod)


def main():
    monkey.patch_thread()

http_server = WSGIServer(('0.0.0.0', 5000), app)
http_server.serve_forever()
