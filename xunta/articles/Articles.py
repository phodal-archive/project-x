from xunta.articles import models


class Article():
    def __init__(self, title=None, description=None, tag=None, content=None, author=None):
        self.author = author
        self.content = content
        self.tag = tag
        self.title = title
        self.description = description
        self.id = None

    def save(self):
        articles = models.Article(title=self.title, description=self.description,
                                  content=self.content, tag=self.tag, author=self.author)
        articles.save()
        print "new articles id = %s " % articles.id
        self.id = articles.id
        return self.id