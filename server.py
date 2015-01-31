import falcon
from gevent.wsgi import WSGIServer

from api.post import PostsResource, AllPostsResource, CommentsResource, PostsCommentsResource

api = falcon.API()

api.add_route('/posts/{post_id}', PostsResource())
api.add_route('/posts/{post_id}/comments', PostsCommentsResource())
api.add_route('/comment/{comment_id}', CommentsResource())
api.add_route('/all/posts', AllPostsResource())

if __name__ == '__main__':
    server = WSGIServer(('0.0.0.0', 8000), api)
    server.serve_forever()