#!/usr/bin/env python
# coding=utf-8

from flask_testing import TestCase, Twill

import twilltestlib
from xunta import create_app


class TestViews(TestCase):
    def create_app(self):
        app = create_app('test')
        self.twill = Twill(app)
        return app

    def test_route(self):
        with self.twill as t:
            self.assert200(self.client.get("/"))
            self.assert200(self.client.get("/sitemap.xml"))

            self.assert200(self.client.get("/register/account"))
            self.assert200(self.client.get("/login"))
            self.assertStatus(self.client.get("/logout"), 302)

            self.assertStatus(self.client.get("/articles"), 301)
            self.assertStatus(self.client.get("/articles/"), 200)

            self.assertStatus(self.client.get("/404"), 404)

    def test_create_account(self):
        with self.twill as t:
            url = self.twill.url("/register/account")
            twilltestlib.execute_twill_script('tests/register.twill', initial_url=url)

    def test_login_account(self):
        with self.twill as t:
            url = self.twill.url("/login")
            twilltestlib.execute_twill_script('tests/login.twill', initial_url=url)
            self.assertStatus(self.client.get("/account"), 200)

            initial_url = self.twill.url("/")
            twilltestlib.execute_twill_script('tests/logout.twill', initial_url=initial_url)