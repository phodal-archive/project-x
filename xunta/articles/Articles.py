from xunta.articles import models
from slugify import slugify


class Article():
    def __init__(self, title=None, description=None, tag=None, content=None, author=None, slug=None):
        self.slug = slug
        self.author = author
        self.content = content
        self.tag = tag
        self.title = title
        self.description = description
        self.id = None

    def save(self):
        slug = self.slug
        if not self.slug:
            slug = slugify(self.title)

        articles = models.Article(title=self.title, description=self.description,
                                  content=self.content, tag=self.tag, author=self.author, slug=slug)
        articles.save()
        return slug


    def get_all_articles(self):
        all_articles = models.Article.objects()
        return all_articles


    def get_article_by_slug(self, slug):
        results = models.Article.objects.get(slug=slug)
        return results


class Tag():
    def __init__(self, name=None, description=None):
        self.description = description
        self.name = name
        self.id = None


    def get_mongo_doc(self):
        if self.id:
            return models.Tag.objects.with_id(self.id)
        else:
            return None

    def save(self):
        new_tag = models.Tag(name=self.name, description=self.description)
        new_tag.save()
        self.id = new_tag.id
        return self.id