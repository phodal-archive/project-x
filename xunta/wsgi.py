from gevent import monkey
from gevent.wsgi import WSGIServer
from xunta import app


def main():
    monkey.patch_thread()

http_server = WSGIServer(('0.0.0.0', 5000), app)
http_server.serve_forever()