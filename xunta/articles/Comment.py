from xunta.articles import models


class Comment():
    def __init__(self, article=None, content=None, user=None, vote=None):
        self.id = None
        self.user = user
        self.content = content
        self.article = article
        self.vote = vote

    def get_mongo_doc(self):
        if self.id:
            return models.Comment.objects.with_id(self.id)
        else:
            return None

    def save(self):
        comment = models.Comment(article=self.article, content=self.content, user=self.user, vote=self.vote)
        comment.save()
        return self.id