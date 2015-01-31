import falcon
from gevent.wsgi import WSGIServer

from api.post import PostsResource, AllPostsResource, CommentsResource, PostsCommentsResource


api = application = falcon.API()

posts = PostsResource()
allPosts = AllPostsResource()
commentsResource = CommentsResource()
postsComments = PostsCommentsResource()

api.add_route('/posts/{post_id}', posts)
api.add_route('/posts/{post_id}/comments', postsComments)
api.add_route('/comment/{comment_id}', commentsResource)
api.add_route('/all/posts', allPosts)

if __name__ == '__main__':
    server = WSGIServer(('0.0.0.0', 8000), api)
    server.serve_forever()