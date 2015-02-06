#!/usr/bin/env python
# coding=utf-8

from twill.browser import TwillException

from flask_testing import TestCase, Twill
from twill.commands import formclear, fv, submit, showforms, show

from xunta import app


class TestViews(TestCase):
    def create_app(self):
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
            # self.assertStatus(self.client.get("/articles/"), 301)

    # def test_bad_manually(self):
        # with self.twill as t:
            # t.browser.go(self.twill.url("/register/account"))
            # t.browser.showforms()
            # formclear('0')
            # fv("0", "name", "test")
            # fv("0", "email", "test@tes.com")
            # fv("0", "password", "testpass")
            # fv("0", "confirm", "testpass")
            # submit()
            # self.assertRaises(TwillException, t.browser.submit, 1)
