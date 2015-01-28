from blog_models import *

posts = WpPosts.get()
if posts is not None:
    print posts.post_title
    print posts.post_content