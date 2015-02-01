from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

from gevent import monkey
from gevent.wsgi import WSGIServer


app = Flask(__name__, static_folder='static', static_url_path='')
app.debug = False

app.config['SECRET_KEY'] = 'I don"t know it'
app.config['DEBUG_TB_PANELS'] = (
    'flask.ext.debugtoolbar.panels.versions.VersionDebugPanel',
    'flask.ext.debugtoolbar.panels.timer.TimerDebugPanel',
    'flask.ext.debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask.ext.debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask.ext.debugtoolbar.panels.template.TemplateDebugPanel',
    'flask.ext.debugtoolbar.panels.logger.LoggingPanel',
    'flask.ext.mongoengine.panels.MongoDebugPanel'
)

app.config['MONGODB_SETTINGS'] = {'DB': 'testing'}
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

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

from users.views import users_mod
app.register_blueprint(users_mod)

def main():
    monkey.patch_thread()

http_server = WSGIServer(('0.0.0.0', 5000), app)
http_server.serve_forever()
