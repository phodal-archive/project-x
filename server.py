import falcon
from flask import Flask
from gevent import monkey
from gevent.pywsgi import WSGIServer

from api.post import PostsResource, AllPostsResource, CommentsResource, PostsCommentsResource

app = Flask(__name__, static_folder='static', static_url_path='')

from frontends.views import mod as frontends_module
app.register_blueprint(frontends_module)

from sitemap.views import mod as sitemap_module
app.register_blueprint(sitemap_module)


api = falcon.API()

api.add_route('/posts/{post_id}', PostsResource())
api.add_route('/posts/{post_id}/comments', PostsCommentsResource())
api.add_route('/comment/{comment_id}', CommentsResource())
api.add_route('/all/posts', AllPostsResource())

#
# def main():
#     monkey.patch_thread()
#
# server = WSGIServer(('0.0.0.0', 8000), api)
# server.serve_forever()
# http_server = WSGIServer(('0.0.0.0', 5000), app)
# http_server.serve_forever()

app.run()