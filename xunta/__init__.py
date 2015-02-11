#!/usr/bin/env python
# coding=utf-8

from flask import Flask, render_template
from flask.ext.wtf import CsrfProtect
from flask_debugtoolbar import DebugToolbarExtension
from flask_babel import Babel
from flask_login import LoginManager
from flask_cache import Cache

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'users.login'
csrf = CsrfProtect()

def create_app(config):
    global app, babel, toolbar, cache, not_found, server_error, frontends_mod, sitemap_mod, db, login_manager, users_mod, articles_mod
    app = Flask(__name__, static_folder='static', static_url_path='')
    app.config.from_pyfile(config + '.cfg')
    babel = Babel(app)
    toolbar = DebugToolbarExtension(app)
    cache = Cache(app)
    csrf.init_app(app)

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def server_error(error):
        return render_template('500.html'), 500

    from xunta.frontends.views import frontends_mod

    app.register_blueprint(frontends_mod)
    from xunta.sitemap.views import sitemap_mod

    app.register_blueprint(sitemap_mod)
    from xunta.users.models import db

    db.init_app(app)
    login_manager.init_app(app)
    from xunta.users.views import users_mod

    app.register_blueprint(users_mod)
    from xunta.articles.views import articles_mod

    app.register_blueprint(articles_mod)

    return app