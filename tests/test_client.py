import re
from flask import url_for
from mongoengine import connect
from suite import BaseSuite
from xunta import create_app


class TestSignup(BaseSuite):
    def setUp(self):
        db = connect('testing')
        db.drop_database('testing')
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=False)

    def tearDown(self):
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get(self.url_for("frontends.home"))
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
        })
        print response.data
        assert "Redirecting..." in response.data
