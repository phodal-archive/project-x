import models


class Article():
    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description
        self.id = None

    def save(self):
        newuser = models.Article(name=self.name, description=self.description)
        newuser.save()
        print "new user id = %s " % newuser.id
        self.id = newuser.id
        return self.id