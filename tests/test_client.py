import re
from flask import url_for
from mongoengine import connect
from suite import BaseSuite
from xunta import create_app
from xunta.articles.Articles import Article, Tag
from xunta.users.User import User


def prepare_account(self):
    with self.app.test_request_context():
        user = User(name='foo', email='foo@email.com', password='1')
        user.save()
        return user


class TestSignup(BaseSuite):
    def setUp(self):
        db = connect('testing')
        db.drop_database('testing')
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=False)
        self.user = prepare_account(self)

    def tearDown(self):
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get(self.url_for("frontends.home"))
        assert response.status_code is 200
        response = self.client.get(self.url_for("sitemap.sitemap"))
        assert response.status_code is 200

    def test_register(self):
        self.client.get(self.url_for("users.logout"))

        response = self.client.post(self.url_for('users.register'), data={
            'name': 'john',
            'email': 'john@example.com',
            'password': 'hello',
            'confirm': 'hello',
        })
        assert "Redirecting..." in response.data

        response = self.client.post(self.url_for('users.login'), data={
            'email': 'john@example.com',
            'password': 'hello'
        }, follow_redirects=True)
        self.client.post(self.url_for('users.logout'))
        assert "wrapper" in response.data


    def prepare_article(self):
        print self.user.email
        self.client.get(self.url_for("articles.create_articles"))
        tag = Tag(name='tag', description='tag description')
        tag.save()
        article = Article(title="title",
                          description="description",
                          content="this is content",
                          slug='hello',
                          author=self.user.get_mongo_doc(),
                          tag=tag.get_mongo_doc())
        article.save()
        for article in article.get_all_articles():
            assert 'description' in article.description