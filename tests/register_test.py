#!/usr/bin/env python
# coding=utf-8

from twill.browser import TwillException

from flask_testing import TestCase, Twill
from twill.commands import formclear, fv, submit, showforms, show
import twilltestlib

from xunta import app


class TestViews(TestCase):
    def create_app(self):
        app.config['MONGODB_SETTINGS'] = {'DB': 'test'}
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

    # def test_create_account(self):
        # with self.twill as t:
            # url = self.twill.url("/register/account")
            # twilltestlib.execute_twill_script('tests/register.twill', initial_url=url)