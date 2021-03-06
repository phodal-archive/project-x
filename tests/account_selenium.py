#!/usr/bin/env python
# coding=utf-8

import unittest
from mongoengine import connect

from selenium import webdriver
from flask_testing import LiveServerTestCase

from xunta import create_app


class Account(LiveServerTestCase):
    def create_app(self):
        app = create_app('test')
        return app

    def setUp(self):
        db = connect('testing')
        db.drop_database('testing')
        self.driver = webdriver.Firefox()

    def test_create_account(self):
        url = "http://localhost:5000/register/account"
        driver = self.driver
        driver.get(url)
        self.assertIn(url, driver.current_url)
        name = driver.find_elements_by_xpath("//input[@name='name']")[0]
        name.send_keys("selenium")
        email = driver.find_elements_by_xpath("//input[@name='email']")[0]
        email.send_keys("selenium@example.com")
        password = driver.find_elements_by_xpath("//input[@name='password']")[0]
        password.send_keys("selenium@example.com")
        confirm = driver.find_elements_by_xpath("//input[@name='confirm']")[0]
        confirm.send_keys("selenium@example.com")
        confirm = driver.find_elements_by_xpath("//input[@name='accept_tos']")[0]
        confirm.click()

        submit_button = driver.find_element_by_name('register')
        submit_button.click()
        self.assertIn("http://localhost:5000", driver.current_url)

    def tearDown(self):
        self.driver.close()

class Login(LiveServerTestCase):
    def create_app(self):
        app = create_app('test')
        return app

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_create_articles_redirect(self):
        url = "http://localhost:5000/login"
        driver = self.driver
        driver.get(url)
        email = driver.find_elements_by_xpath("//input[@name='email']")[0]
        email.send_keys("selenium@example.com")
        password = driver.find_elements_by_xpath("//input[@name='password']")[0]
        password.send_keys("selenium@example.com")
        submit_button = driver.find_element_by_name('login')
        submit_button.click()
        self.assertIn("http://localhost:5000", driver.current_url)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
