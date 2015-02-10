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

    def get_all_comments(self):
        all_comments = models.Comment.objects()
        return all_comments


    def get_comment_by_article(self, article):
        all_comments = models.Comment.objects(article=article)
        return all_comments

    def save(self):
        comment = models.Comment(article=self.article, content=self.content, user=self.user, vote=self.vote)
        comment.save()
        self.id = comment.id
        return self.id