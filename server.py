import falcon
from blog_models import *


class PostsResource():
    def __init__(self):
        pass

    @staticmethod
    def on_get(req, resp, post_id):
        post = WpPosts.get(WpPosts.id == post_id)
        resp.status = falcon.HTTP_200
        resp.body = post.post_content


app = application = falcon.API()

posts = PostsResource()
app.add_route('/posts/{post_id}', posts)