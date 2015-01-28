import falcon
from blog_models import *


class PostsResource:
    def __init__(self):
        pass

    @staticmethod
    def on_get(req, resp):
        posts = WpPosts.get()
        resp.status = falcon.HTTP_200
        resp.body = posts.post_content


app = falcon.API()

app.add_route('/things', PostsResource())