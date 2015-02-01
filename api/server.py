import falcon
from post import PostsResource, AllPostsResource, CommentsResource, PostsCommentsResource
from gevent import monkey
from gevent.wsgi import WSGIServer


def main():
    monkey.patch_thread()


api = falcon.API()

api.add_route('/posts/{post_id}', PostsResource())
api.add_route('/posts/{post_id}/comments', PostsCommentsResource())
api.add_route('/comment/{comment_id}', CommentsResource())
api.add_route('/all/posts', AllPostsResource())

server = WSGIServer(('0.0.0.0', 8000), api)
server.serve_forever()