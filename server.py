import falcon
from gevent.wsgi import WSGIServer

from api.post import PostsResource, AllPostsResource, CommentsResource, PostsCommentsResource


app = application = falcon.API()

posts = PostsResource()
allPosts = AllPostsResource()
commentsResource = CommentsResource()
postsComments = PostsCommentsResource()

app.add_route('/posts/{post_id}', posts)
app.add_route('/posts/{post_id}/comments', postsComments)
app.add_route('/comment/{comment_id}', commentsResource)
app.add_route('/all/posts', allPosts)

if __name__ == '__main__':
    server = WSGIServer(('0.0.0.0', 8000), app)
    server.serve_forever()