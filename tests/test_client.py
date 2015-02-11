import re
from flask import url_for
from suite import BaseSuite
from xunta import create_app


class TestSignup(BaseSuite):
    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get(self.url_for("frontends.home"))
    #
    # def test_register_and_login(self):
    #     # register a new account
    #     response = self.client.post(url_for('auth.register'), data={
    #         'email': 'john@example.com',
    #         'username': 'john',
    #         'password': 'cat',
    #         'password2': 'cat'
    #     })
    #     self.assertTrue(response.status_code == 302)
    #
    #     # login with the new account
    #     response = self.client.post(url_for('user.login'), data={
    #         'email': 'john@example.com',
    #         'password': 'cat'
    #     }, follow_redirects=True)
    #     self.assertTrue(re.search(b'Hello,\s+john!', response.data))
    #     self.assertTrue(
    #         b'You have not confirmed your account yet' in response.data)