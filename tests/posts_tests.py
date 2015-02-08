#!/usr/bin/env python
# coding=utf-8

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_create_articles_redirect(self):
        url = "http://127.0.0.1:5000/create/articles"
        driver = self.driver
        driver.get(url)
        self.assertIn("http://127.0.0.1:5000/login", driver.current_url)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
