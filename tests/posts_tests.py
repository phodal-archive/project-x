#!/usr/bin/env python
# coding=utf-8

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Account(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_create_account(self):
        url = "http://127.0.0.1:5000/register/account"
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
        self.assertIn("http://127.0.0.1:5000", driver.current_url)

    def tearDown(self):
        self.driver.close()

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
