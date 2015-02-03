#!/usr/bin/env python
#coding=utf-8

from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_babel import Babel
from flask_login import LoginManager

from gevent import monkey
from gevent.wsgi import WSGIServer


app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_pyfile('config.cfg')

babel = Babel(app)
toolbar = DebugToolbarExtension(app)

login_manager = LoginManager()

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def not_found(error):
    return render_template('500.html'), 500

from frontends.views import mod as frontends_module
app.register_blueprint(frontends_module)

from sitemap.views import mod as sitemap_module
app.register_blueprint(sitemap_module)

from users.models import db
db.init_app(app)
login_manager.init_app(app)

from users.views import users_mod
app.register_blueprint(users_mod)

def main():
    monkey.patch_thread()

http_server = WSGIServer(('0.0.0.0', 5000), app)
http_server.serve_forever()
