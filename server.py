from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

from gevent import monkey
from gevent.wsgi import WSGIServer


app = Flask(__name__, static_folder='static', static_url_path='')
app.debug = True

app.config['SECRET_KEY'] = 'I don"t know it'
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


def main():
    monkey.patch_thread()

http_server = WSGIServer(('0.0.0.0', 5000), app)
http_server.serve_forever()