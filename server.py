import falcon
from flask import Flask, request, send_from_directory
from gevent.pywsgi import WSGIServer

from api.post import PostsResource, AllPostsResource, CommentsResource, PostsCommentsResource


app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.static_folder, request.path[1:])

    return response


api = falcon.API()

api.add_route('/posts/{post_id}', PostsResource())
api.add_route('/posts/{post_id}/comments', PostsCommentsResource())
api.add_route('/comment/{comment_id}', CommentsResource())
api.add_route('/all/posts', AllPostsResource())
#
# if __name__ == '__main__':
#     server = WSGIServer(('0.0.0.0', 8000), api)
#     server.serve_forever()

if __name__ == "__main__":
    app.run()